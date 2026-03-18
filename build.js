const fs = require('fs');
const path = require('path');
const { marked } = require('marked');

const inputDir = __dirname;
const outputDir = path.join(__dirname, 'dist');
const srcDir = path.join(__dirname, 'src');

// Create required directories
if (!fs.existsSync(outputDir)) {
    fs.mkdirSync(outputDir, { recursive: true });
}

// Ensure resources exist
const templatePath = path.join(srcDir, 'template.html');
const cssPath = path.join(srcDir, 'styles.css');

if (!fs.existsSync(templatePath)) {
    console.error("Template HTML missing!");
    process.exit(1);
}

// Copy CSS to dist
fs.copyFileSync(cssPath, path.join(outputDir, 'styles.css'));

// Read template
const templateHtml = fs.readFileSync(templatePath, 'utf-8');

// Get all markdown files
function getAllMarkdownFiles(dir, fileList = []) {
    const files = fs.readdirSync(dir);
    for (const file of files) {
        const filePath = path.join(dir, file);
        if (filePath.includes('node_modules') || filePath.includes('.git') || filePath.includes('dist') || filePath.includes('src')) continue;
        
        if (fs.statSync(filePath).isDirectory()) {
            getAllMarkdownFiles(filePath, fileList);
        } else if (filePath.endsWith('.md')) {
            fileList.push(filePath);
        }
    }
    return fileList;
}

const mdFiles = getAllMarkdownFiles(inputDir);

// Construct Navigation Info
const navData = {
    companies: [],
    phases: [],
    learning: [],
    root: []
};

mdFiles.forEach(file => {
    let rel = path.relative(inputDir, file).replace(/\\/g, '/');
    const titleMatch = fs.readFileSync(file, 'utf8').match(/^#\s+(.*)/m);
    const title = titleMatch ? titleMatch[1] : path.basename(file, '.md');
    
    const outRel = rel.replace(/\.md$/, '.html');
    
    const item = { in: file, relIn: rel, relOut: outRel, title };

    if (rel.startsWith('companies/')) {
        // Only include standard READMEs or specific files to prevent clutter
        if (rel.endsWith('README.md') || rel === 'companies/sovereign-edit.md') navData.companies.push(item);
    } else if (rel.startsWith('docs/phases/')) {
        navData.phases.push(item);
    } else if (rel.startsWith('learning/')) {
        // Use directory name as title for 'notes.md' for better sidebar UX
        if (rel.endsWith('notes.md') || rel.endsWith('README.md')) {
            const dirName = path.basename(path.dirname(file));
            // Capitalize and format directory name
            item.title = dirName.split('-').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
        }
        navData.learning.push(item);
    } else {
        navData.root.push(item);
    }
});

// Build Sidebar HTML
let sidebarHtml = `
<div class="nav-group">
    <div class="nav-group-title">Overview</div>
    <ul class="nav-list">
        <li><a href="index.html">Home</a></li>
    </ul>
</div>
`;

if(navData.companies.length > 0) {
    sidebarHtml += `<div class="nav-group"><div class="nav-group-title">The 9 Companies</div><ul class="nav-list">`;
    navData.companies.forEach(i => { sidebarHtml += `<li><a href="${i.relOut}">${i.title.replace('The Sovereign Stack: ', '').replace('The ', '')}</a></li>` });
    sidebarHtml += `</ul></div>`;
}

if(navData.phases.length > 0) {
    sidebarHtml += `<div class="nav-group"><div class="nav-group-title">Phases</div><ul class="nav-list">`;
    navData.phases.forEach(i => { sidebarHtml += `<li><a href="${i.relOut}">${i.title}</a></li>` });
    sidebarHtml += `</ul></div>`;
}

if(navData.learning.length > 0) {
    sidebarHtml += `<div class="nav-group"><div class="nav-group-title">Learning</div><ul class="nav-list">`;
    navData.learning.forEach(i => { sidebarHtml += `<li><a href="${i.relOut}">${i.title}</a></li>` });
    sidebarHtml += `</ul></div>`;
}

// Convert files
mdFiles.forEach(file => {
    let rel = path.relative(inputDir, file).replace(/\\/g, '/');
    let outRel = rel.replace(/\.md$/, '.html');
    
    // special rule for README.md -> index.html
    if (rel === 'README.md') {
        outRel = 'index.html';
    }

    const outPath = path.join(outputDir, outRel);
    const outDir = path.dirname(outPath);
    if (!fs.existsSync(outDir)) fs.mkdirSync(outDir, { recursive: true });

    let mdSrc = fs.readFileSync(file, 'utf8');

    // Fix internal links to point to .html from .md
    // Regex matching [text](./path/to/file.md) or [text](/path/to/file.md) or [text](path.md)
    mdSrc = mdSrc.replace(/\[([^\]]+)\]\(([^)]+\.md)\)/g, (match, p1, p2) => {
        return `[${p1}](${p2.replace(/\.md$/, '.html')})`;
    });

    // Special fix for README.md links turning into index.html
    mdSrc = mdSrc.replace(/href="([^"]*)README\.html"/g, 'href="$1index.html"'); 
    mdSrc = mdSrc.replace(/\[([^\]]+)\]\(([^)]*)README\.html\)/g, `[$1]($2index.html)`);
    // Ensure root README.md links specifically map to index.html
    mdSrc = mdSrc.replace(/\[([^\]]+)\]\(([^)]*)README\.md\)/g, `[$1]($2index.html)`);

    const htmlContent = marked.parse(mdSrc);

    // Get depth for asset base path
    const depth = outRel.split('/').length - 1;
    const rootPath = depth === 0 ? './' : '../'.repeat(depth);

    // Replace absolute-ish paths in sidebar with relative ones
    const relativeSidebar = sidebarHtml.replace(/href="\//g, `href="${rootPath}`);

    // Get title
    const titleMatch = mdSrc.match(/^#\s+(.*)/m);
    const title = titleMatch ? titleMatch[1] : path.basename(file, '.md');

    let finalHtml = templateHtml
        .replace(/\{\{TITLE\}\}/g, title)
        .replace(/\{\{SIDEBAR\}\}/g, relativeSidebar)
        .replace(/\{\{CONTENT\}\}/g, htmlContent)
        .replace(/href="\/styles.css"/g, `href="${rootPath}styles.css"`);

    // Ensure link in root index.html to companies/veridact/ resolves properly, marked produces `<a href="./companies/veridact/">`
    // We should ensure people who click dir links go to the index or README.html equivalent inside that dir
    // Since we generate README.html for dirs if README.md exists, let's fix directory links to point to README.html
    finalHtml = finalHtml.replace(/href="([^"]+\/)"/g, 'href="$1README.html"');

    fs.writeFileSync(outPath, finalHtml);
    console.log(`Generated: ${outRel}`);
});

console.log("Static site generation complete!");
