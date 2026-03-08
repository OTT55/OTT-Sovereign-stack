# PHASE 2: TECHNICAL DEPTH (2028–2030)
### "Build the primitives before you build the product."

## OBJECTIVE
Go from understanding to implementation. Build toy versions of every core protocol.

## WHAT TO EXPECT
- This is the hardest phase. ZK circuits are genuinely difficult.
- You will build things that don't work. That is the work.
- By end of phase: you have working prototypes of Veridact and Nullform at toy scale.
- Your films now demonstrate the protocols in action.

## LEARNING TRACKS

### 1. Zero-Knowledge Proofs (Implementation)
- [ ] Understand the prover/verifier architecture
- [ ] Learn arithmetic circuits
- [ ] Write circuits in Circom
- [ ] Move to arkworks (Rust ZK library)
- [ ] Build: proof-of-location without revealing location
- [ ] Build: proof-of-human-capture without revealing identity

**Resources:**
- *Proofs, Arguments, and Zero-Knowledge* — Justin Thaler (free PDF)
- ZKHack puzzles (zkiap.com) — hands-on ZK challenges
- arkworks-rs documentation (GitHub)
- Circom documentation (docs.circom.io)
- 0xPARC learning resources (learn.0xparc.org)

**Milestone:** Working Circom circuit that proves a photo timestamp without revealing it.

---

### 2. Trusted Execution Environments (TEEs)
- [ ] ARM TrustZone architecture
- [ ] Intel SGX programming model
- [ ] Understand attack surface (what TEEs protect vs. don't)
- [ ] Build a simple attestation demo

**Resources:**
- Intel SGX Developer Guide (free, Intel documentation)
- *A Primer on Hardware Security* — academic papers via Google Scholar
- Teaclave (Apache) — open source TEE framework
- ARM TrustZone developer documentation

**Milestone:** A demo where data processed inside an enclave produces an unforgeable attestation report.

---

### 3. Smart Contracts & Blockchain
- [ ] Solidity basics (read and audit level)
- [ ] StarkNet / Cairo (ZK-native — directly relevant to your stack)
- [ ] How a revenue waterfall works as code
- [ ] ERC standards relevant to IP and rights

**Resources:**
- CryptoZombies (free, Solidity tutorial)
- StarkNet documentation (docs.starknet.io)
- *Mastering Ethereum* — Antonopoulos (free on GitHub)
- OpenZeppelin contracts (reference implementations)

**Milestone:** Deploy a simple rights registry contract on StarkNet testnet.

---

### 4. AI/ML Engineering
- [ ] How transformer models work at the architecture level
- [ ] Fine-tuning open-source models (Mistral, Llama)
- [ ] RAG (Retrieval Augmented Generation) — core of ContextCore
- [ ] Vector databases (Pinecone, Chroma, Weaviate)
- [ ] Data pipeline engineering

**Resources:**
- *Attention Is All You Need* — Vaswani et al. (original paper, free)
- Andrej Karpathy YouTube — build GPT from scratch (free)
- Fast.ai practical deep learning course (free)
- LangChain documentation (for RAG pipelines)
- Hugging Face tutorials (free)

**Milestone:** Fine-tune Mistral on 500 pages of film production accounting documents. Demonstrate it outperforms GPT-4 on domain-specific questions.

---

### 5. Filmmaking
- [ ] Direct first feature-length or long short (30–60 min)
- [ ] Run it through every conceptual protocol (manual provenance chain)
- [ ] Attempt first international distribution (even micro-scale)
- [ ] Document every friction point — each one is a product specification

**Milestone:** Feature/long short completed and distributed. Friction log documented in repo.

---

## DELIVERABLES BY END OF PHASE 2
- [ ] Toy ZK proof for media attestation (Veridact prototype)
- [ ] TEE attestation demo
- [ ] Rights registry on testnet (Canonchain prototype)
- [ ] Fine-tuned domain model (ContextCore prototype)
- [ ] One feature/long short film completed

