"""
Mock Interview Agent - Question Bank
Provides rich, curated question sets for Demo Mode across multiple roles, types, and difficulties.
Each question includes keywords, evaluation criteria, and exemplary sample answers.
"""

QUESTION_BANK = [
    # =========================================================================
    # JAVA DEVELOPER - TECHNICAL
    # =========================================================================
    # Beginner
    {
        "id": "java_tech_beg_1",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Core Java / OOP",
        "question": "Can you explain the difference between JDK, JRE, and JVM in Java, and why Java is considered platform-independent?",
        "keywords": ["jvm", "jre", "jdk", "bytecode", "platform-independent", "write once run anywhere", "compiler", "operating system"],
        "ideal_concepts": ["JDK contains JRE and development tools like javac", "JRE provides runtime environment and libraries", "JVM executes bytecode", "Bytecode is platform-independent while JVM is platform-dependent"],
        "sample_answer": "JDK (Java Development Kit) is the complete software package for developing Java applications, including the compiler (javac) and debugger. JRE (Java Runtime Environment) contains the libraries and runtime needed solely to run compiled programs. JVM (Java Virtual Machine) is the core engine that executes Java bytecode.\n\nJava achieves platform independence through its 'Write Once, Run Anywhere' (WORA) philosophy: source code is compiled into bytecode (.class files), which any platform-specific JVM can translate into native machine instructions."
    },
    {
        "id": "java_tech_beg_2",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "OOP Principles",
        "question": "What are the four core principles of Object-Oriented Programming (OOP) in Java? Provide a brief code-level example or explanation for one of them.",
        "keywords": ["encapsulation", "inheritance", "polymorphism", "abstraction", "class", "object", "getter", "setter", "override", "interface"],
        "ideal_concepts": ["Encapsulation binds data and methods together with private access", "Inheritance allows code reuse via extends", "Polymorphism enables method overloading and overriding", "Abstraction hides implementation details using abstract classes and interfaces"],
        "sample_answer": "The four core pillars of OOP in Java are Encapsulation, Abstraction, Inheritance, and Polymorphism.\n\nFor example, Encapsulation restricts direct access to an object's fields using private access modifiers and provides controlled access through public getters and setters. This prevents invalid state changes and decouples internal data representation from external consumers."
    },
    {
        "id": "java_tech_beg_3",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Memory / Strings",
        "question": "What is the difference between '==' and '.equals()' in Java? Why are Strings immutable in Java?",
        "keywords": ["==", "equals", "reference", "memory", "string pool", "immutable", "thread-safe", "security", "heap"],
        "ideal_concepts": ["'==' compares memory references while .equals() compares value/content", "Strings are immutable for security, string pooling/caching, and thread safety"],
        "sample_answer": "In Java, '==' compares memory addresses (object references), while '.equals()' compares the actual value or content of the objects.\n\nStrings are immutable (cannot be modified after creation) for three primary reasons: 1) String Pool efficiency and memory optimization, 2) Thread safety, since immutable objects can be shared across threads without synchronization, and 3) Security, as strings are heavily used for network sockets, file paths, and database connections."
    },
    {
        "id": "java_tech_beg_4",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Collections",
        "question": "What is the difference between an ArrayList and a LinkedList in Java? When would you choose one over the other?",
        "keywords": ["arraylist", "linkedlist", "dynamic array", "doubly linked", "index", "o(1)", "o(n)", "insertion", "deletion", "contiguous"],
        "ideal_concepts": ["ArrayList is backed by dynamic array, O(1) random access, slower insertions in the middle", "LinkedList is doubly-linked list, O(1) insertions/deletions at ends, O(n) traversal for index access", "Memory overhead difference"],
        "sample_answer": "ArrayList is implemented as a resizable array, offering fast O(1) time complexity for random access/retrieval by index, but O(n) for inserting or deleting elements from the middle due to element shifting. In contrast, LinkedList is implemented as a doubly-linked list, providing fast O(1) insertions and deletions once an element is located, but O(n) traversal time to find an element by index.\n\nI would choose ArrayList when read operations dominate, and LinkedList when frequent insertions and deletions at boundaries occur without needing indexed lookups."
    },
    {
        "id": "java_tech_beg_5",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Exception Handling",
        "question": "Explain the difference between Checked and Unchecked exceptions in Java. How does the try-catch-finally block work?",
        "keywords": ["checked", "unchecked", "runtimeexception", "compile-time", "try", "catch", "finally", "throwable", "ioexception"],
        "ideal_concepts": ["Checked exceptions are checked at compile time and must be handled or declared with throws", "Unchecked exceptions inherit from RuntimeException and occur at runtime", "Finally block always executes regardless of exceptions"],
        "sample_answer": "Checked exceptions (e.g., IOException, SQLException) are verified at compile time, meaning the compiler forces the developer to handle them using try-catch or declare them using throws. Unchecked exceptions (subclasses of RuntimeException, like NullPointerException, ArrayIndexOutOfBoundsException) occur at runtime and represent programming logic errors.\n\nThe try block holds code that may throw an exception, catch blocks handle specific exceptions, and the finally block executes unconditionally for cleanup operations like closing file handles or database connections."
    },

    # Intermediate
    {
        "id": "java_tech_int_1",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Multithreading & Concurrency",
        "question": "How does Java manage multithreading? Explain the difference between implementing 'Runnable' vs extending 'Thread', and what the 'synchronized' keyword accomplishes.",
        "keywords": ["runnable", "thread", "synchronized", "multithreading", "lock", "race condition", "executor", "concurrency", "interface"],
        "ideal_concepts": ["Implementing Runnable is preferred because Java only supports single class inheritance", "Thread lifecycle (new, runnable, blocked, waiting, terminated)", "synchronized ensures mutual exclusion and thread-safe critical sections"],
        "sample_answer": "In Java, a thread can be created by extending the Thread class or implementing the Runnable interface. Implementing Runnable is standard practice because Java does not support multiple inheritance, allowing your class to extend other domain classes, and it decouples task logic from thread execution (ideal for ExecutorService thread pools).\n\nThe 'synchronized' keyword enforces mutual exclusion. When a method or block is synchronized, a thread must acquire the intrinsic monitor lock of the object before entering, preventing race conditions when accessing shared mutable state."
    },
    {
        "id": "java_tech_int_2",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Collections & Hashing",
        "question": "How does a HashMap work internally in Java? What happens during a hash collision, and why was treeification introduced in Java 8?",
        "keywords": ["hashmap", "hashcode", "equals", "bucket", "collision", "linked list", "red-black tree", "treeify", "load factor", "o(1)"],
        "ideal_concepts": ["HashMap uses an array of buckets", "hashCode() determines bucket index", "equals() resolves keys within the bucket", "Java 8 converts linked list to red-black tree when bucket exceeds 8 entries, reducing worst case from O(n) to O(log n)"],
        "sample_answer": "A HashMap internally uses an array of Node buckets. When put(K, V) is called, Java computes the key's hashCode(), applies an internal hash distribution function, and determines the bucket index. If multiple keys map to the same bucket, a hash collision occurs.\n\nPrior to Java 8, collisions were resolved via a singly-linked list, causing worst-case lookup to degrade to O(n). In Java 8, once a bucket exceeds the TREEIFY_THRESHOLD (8 entries) and the total capacity is at least 64, the bucket transforms into a balanced Red-Black Tree, improving worst-case search complexity to O(log n)."
    },
    {
        "id": "java_tech_int_3",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Java 8+ Features",
        "question": "Explain Java Streams and Lambda expressions. How do intermediate operations differ from terminal operations in a Stream pipeline?",
        "keywords": ["stream", "lambda", "functional interface", "filter", "map", "reduce", "collect", "lazy evaluation", "intermediate", "terminal"],
        "ideal_concepts": ["Lambda expressions provide concise syntax for functional interfaces", "Streams enable declarative data processing over collections", "Intermediate operations (filter, map) are lazy and return a new Stream", "Terminal operations (collect, forEach, reduce) trigger execution and produce a result"],
        "sample_answer": "Introduced in Java 8, Lambda expressions allow passing anonymous functions as first-class citizens using functional interfaces. Streams provide a declarative pipeline to process sequences of elements without modifying the underlying source collection.\n\nThe key distinction is lazy evaluation: Intermediate operations (e.g., filter(), map(), sorted()) are lazy; they return another Stream and do not execute until a terminal operation is invoked. Terminal operations (e.g., collect(), forEach(), count(), reduce()) execute the pipeline, consume the stream, and produce a final non-stream result."
    },
    {
        "id": "java_tech_int_4",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Memory Management",
        "question": "How does Garbage Collection work in Java? Describe the difference between Heap and Stack memory.",
        "keywords": ["garbage collection", "heap", "stack", "young generation", "old generation", "eden", "mark and sweep", "gc", "out of memory"],
        "ideal_concepts": ["Stack memory stores local primitive variables and method call frames (LIFO)", "Heap memory stores all objects and class instances", "Generational hypothesis: Eden, Survivor spaces, Tenured/Old generation", "Mark, sweep, and compact algorithms"],
        "sample_answer": "In Java, Stack memory is thread-local and manages method call frames, local primitives, and references to objects; it operates in LIFO order and is automatically cleared when methods return. Heap memory is shared across all threads and stores all instantiated objects.\n\nGarbage Collection (GC) automatically reclaims heap memory occupied by unreferenced objects using the Generational Hypothesis. The heap is divided into Young Generation (Eden and Survivor spaces) and Old/Tenured Generation. New objects are allocated in Eden; survivors of Minor GCs are copied to survivor spaces and eventually promoted to Old Generation, which is reclaimed by Major/Full GCs."
    },
    {
        "id": "java_tech_int_5",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Frameworks / Spring",
        "question": "What is Dependency Injection and Inversion of Control (IoC) in the Spring Framework, and why is it beneficial?",
        "keywords": ["dependency injection", "inversion of control", "ioc container", "spring", "autowired", "decoupling", "unit test", "mocking"],
        "ideal_concepts": ["IoC shifts object lifecycle control from application code to the framework container", "Dependency Injection is a pattern implementing IoC by supplying dependencies via constructor or setter", "Benefits include loose coupling, high testability, and separation of concerns"],
        "sample_answer": "Inversion of Control (IoC) is a design principle where the control of object creation and lifecycle management is transferred from the program code to an external container (the Spring IoC Container). Dependency Injection (DI) is the specific design pattern that implements IoC by injecting dependent objects into a class (via constructor, setter, or field injection) rather than the class creating them with 'new'.\n\nThis provides loose coupling between components, eliminates hardcoded dependencies, and makes unit testing straightforward because dependencies can easily be swapped with mocks."
    },

    # Advanced
    {
        "id": "java_tech_adv_1",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "JVM Internals & Performance",
        "question": "Explain the Java Memory Model (JMM), the 'volatile' keyword, and how CPU cache coherence (happens-before relationship) is maintained.",
        "keywords": ["jmm", "volatile", "happens-before", "cpu cache", "visibility", "reordering", "memory barrier", "atomic", "instruction reordering"],
        "ideal_concepts": ["JMM specifies interaction between threads and main memory", "volatile guarantees visibility and prevents instruction reordering", "happens-before guarantees memory visibility between write and read", "volatile does NOT guarantee atomicity for compound operations"],
        "sample_answer": "The Java Memory Model (JMM) defines how threads interact through main memory and local CPU caches, resolving visibility and instruction reordering issues.\n\nThe 'volatile' keyword provides two crucial guarantees: 1) Visibility: writes to a volatile variable are immediately flushed to main memory, and reads fetch the freshest value from main memory rather than a thread's CPU cache. 2) Instruction ordering: the compiler and CPU insert memory barriers (fences) preventing reordering across the volatile access. Under the 'happens-before' specification, a write to a volatile variable happens-before every subsequent read of that variable. However, volatile does not guarantee atomicity for compound operations like count++ (which requires AtomicInteger or locks)."
    },
    {
        "id": "java_tech_adv_2",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "High Concurrency",
        "question": "What is the difference between Synchronized blocks, ReentrantLock, and ReadWriteLock? When would you use StampedLock or Atomic primitives?",
        "keywords": ["reentrantlock", "readwritelock", "stampedlock", "atomic", "cas", "lock-free", "fairness", "trylock", "optimistic read"],
        "ideal_concepts": ["ReentrantLock offers timed lock attempts (tryLock), interruptible locks, and fairness policies", "ReadWriteLock separates read and write locks for read-heavy workloads", "StampedLock provides optimistic reading to minimize lock contention", "Atomics use hardware-level Compare-And-Swap (CAS) without kernel context switching"],
        "sample_answer": "While 'synchronized' is implicit and automatically released, 'ReentrantLock' provides advanced capabilities like interruptible locking, timed lock acquisition (tryLock()), and fair locking queues. 'ReadWriteLock' (ReentrantReadWriteLock) separates shared read locks from exclusive write locks, significantly enhancing throughput in read-heavy applications.\n\n'StampedLock' (introduced in Java 8) improves upon ReadWriteLock by supporting optimistic reads where no read lock is acquired unless a concurrent write validates the stamp. For single counters or flags, Atomic classes (AtomicInteger, AtomicReference) should be used because they leverage hardware CAS (Compare-And-Swap) instructions, delivering non-blocking, lock-free performance without kernel context switches."
    },
    {
        "id": "java_tech_adv_3",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Modern Java Architecture",
        "question": "Explain Virtual Threads (Project Loom) in Java 21+. How do they differ from platform threads, and how do they change high-throughput I/O architectures?",
        "keywords": ["virtual threads", "project loom", "platform threads", "carrier thread", "thread-per-request", "unpark", "blocking i/o", "reactive"],
        "ideal_concepts": ["Platform threads are 1:1 mapped to OS threads with heavy memory (~1MB stack)", "Virtual threads are lightweight user-mode threads managed by JVM", "When virtual thread blocks on I/O, JVM unmounts it from carrier thread", "Enables clean synchronous thread-per-request model without reactive complexity"],
        "sample_answer": "Platform threads are 1:1 wrappers around operating system threads, carrying significant memory overhead (~1MB per stack) and expensive context switches, typically capping a server at thousands of concurrent threads. Virtual threads (Java 21 Project Loom) are lightweight user-mode threads scheduled by the JVM over a small pool of carrier OS threads.\n\nWhen a virtual thread executes a blocking I/O operation (like a database query or HTTP call), the JVM unmounts it from its carrier thread and parks it in heap memory, allowing the carrier thread to serve other tasks. Once I/O completes, the virtual thread is rescheduled. This revives the intuitive, readable 'thread-per-request' programming model for millions of concurrent connections without needing complex reactive programming frameworks (like WebFlux)."
    },
    {
        "id": "java_tech_adv_4",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Distributed Systems & Microservices",
        "question": "How do you handle distributed transactions and consistency across Java microservices? Explain the Saga pattern vs Two-Phase Commit (2PC).",
        "keywords": ["saga", "2pc", "two phase commit", "eventual consistency", "compensating transaction", "choreography", "orchestration", "kafka", "acid"],
        "ideal_concepts": ["2PC provides strict ACID but introduces locking, high latency, and single point of failure", "Saga pattern decomposes transaction into local steps with compensating rollbacks", "Saga orchestration vs choreography", "Eventual consistency using event brokers like Kafka or RabbitMQ"],
        "sample_answer": "In distributed microservices, traditional Two-Phase Commit (2PC) is rarely suitable because it requires blocking distributed locks across services and databases, severely hurting availability and throughput (CAP theorem).\n\nInstead, the Saga pattern is preferred. A Saga splits a distributed transaction into a sequence of local transactions. Each local transaction updates its own database and publishes an event or message. If a step fails, the Saga executes compensating transactions in reverse to undo preceding changes.\n\nSagas can be implemented via Orchestration (a central orchestrator coordinates each service) or Choreography (services react to domain events via Kafka/RabbitMQ). This achieves eventual consistency without distributed locking."
    },
    {
        "id": "java_tech_adv_5",
        "role": "Java Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Troubleshooting & Profiling",
        "question": "How would you diagnose and resolve a severe memory leak or CPU spike in a production Java application running in Kubernetes?",
        "keywords": ["memory leak", "heap dump", "thread dump", "jstack", "jmap", "visualvm", "jfr", "profiling", "oom", "garbage collection"],
        "ideal_concepts": ["Capturing thread dumps (jstack) to identify busy loops or deadlocks", "Capturing heap dumps (jcmd/jmap, -XX:+HeapDumpOnOutOfMemoryError)", "Using Java Flight Recorder (JFR) and JDK Mission Control for low overhead profiling", "Analyzing leak suspects (static references, unclosed resources, cache accumulation)"],
        "sample_answer": "To diagnose production issues: For high CPU, I take consecutive thread dumps using 'jstack' or 'jcmd' and correlate top Linux thread IDs (converted to hex) with thread dump nid values to find runaway loops, lock contention, or excessive GC activity.\n\nFor memory leaks, I configure JVM flags like '-XX:+HeapDumpOnOutOfMemoryError -XX:HeapDumpPath=...' and inspect the heap dump with tools like Eclipse Memory Analyzer (MAT) to identify dominant leak suspects, such as unbounded static collections, unclosed streams, or un-evicted cache items. For low-overhead continuous monitoring in Kubernetes, I enable Java Flight Recorder (JFR) and stream metrics to Prometheus and Grafana."
    },

    # =========================================================================
    # WEB DEVELOPER - TECHNICAL
    # =========================================================================
    # Beginner
    {
        "id": "web_tech_beg_1",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "HTML / CSS Basics",
        "question": "What is semantic HTML, why is it important, and how does the CSS Box Model work?",
        "keywords": ["semantic", "header", "footer", "article", "nav", "accessibility", "seo", "box model", "content", "padding", "border", "margin"],
        "ideal_concepts": ["Semantic HTML uses meaningful tags (article, nav, section, main) instead of generic divs", "Benefits: Accessibility (screen readers) and SEO", "CSS Box Model consists of content, padding, border, and margin", "box-sizing: border-box"],
        "sample_answer": "Semantic HTML means using tags that convey the meaning of the content, such as `<header>`, `<nav>`, `<main>`, `<article>`, and `<footer>`, rather than generic `<div>` tags. It improves accessibility for assistive technologies like screen readers and helps search engines index content accurately for SEO.\n\nThe CSS Box Model dictates the layout of every element on a web page, comprising four layers from inside out: Content, Padding (space around content), Border (boundary around padding), and Margin (external spacing separating the element from neighbors). Using `box-sizing: border-box` ensures padding and borders are included within the declared width."
    },
    {
        "id": "web_tech_beg_2",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "JavaScript Fundamentals",
        "question": "What is the difference between 'var', 'let', and 'const' in JavaScript? How does variable hoisting work?",
        "keywords": ["var", "let", "const", "scope", "function scope", "block scope", "hoisting", "temporal dead zone", "tdz", "reassign"],
        "ideal_concepts": ["var is function-scoped and hoisted with undefined", "let and const are block-scoped and hoisted into Temporal Dead Zone", "const cannot be reassigned", "Hoisting moves declarations to top of scope during compilation"],
        "sample_answer": "'var' is function-scoped, can be re-declared, and is hoisted with an initial value of 'undefined'. 'let' and 'const' are block-scoped (confined to curly braces `{}`), cannot be re-declared in the same scope, and are hoisted into a 'Temporal Dead Zone' (TDZ) where accessing them prior to their declaration throws a ReferenceError.\n\n'const' requires an immediate value upon declaration and cannot be reassigned, although properties of objects assigned to const can still be mutated."
    },
    {
        "id": "web_tech_beg_3",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "CSS Layout",
        "question": "Explain the difference between CSS Flexbox and CSS Grid. When would you use one over the other?",
        "keywords": ["flexbox", "grid", "1d", "2d", "one-dimensional", "two-dimensional", "row", "column", "layout", "responsive"],
        "ideal_concepts": ["Flexbox is one-dimensional (row OR column)", "Grid is two-dimensional (simultaneous rows AND columns)", "Flexbox is ideal for component-level alignment and distribution", "Grid is ideal for overall page layout and matrix alignment"],
        "sample_answer": "The primary distinction is dimensional scope: Flexbox is one-dimensional, designed for aligning content along a single axis (either horizontally as a row or vertically as a column). CSS Grid is two-dimensional, engineered to manage rows and columns simultaneously.\n\nI use Flexbox for component-level layouts such as navigation bars, form controls, and button groups where items adapt to content size. I use CSS Grid for page-level layouts, photo galleries, dashboards, and structured multi-column matrices where strict row-column alignment is required."
    },
    {
        "id": "web_tech_beg_4",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "DOM & Events",
        "question": "What is Event Bubbling and Event Capturing in the JavaScript DOM? How does Event Delegation take advantage of this?",
        "keywords": ["event bubbling", "event capturing", "event delegation", "target", "currenttarget", "stoppropagation", "addeventlistener", "parent"],
        "ideal_concepts": ["Event flow has 3 phases: capturing (top-down), target, bubbling (bottom-up)", "Event delegation attaches one listener to a common parent to handle children dynamically", "Saves memory and handles dynamically added elements"],
        "sample_answer": "When an event occurs in the DOM, it travels in three phases: Capturing (down from document root to target element), Target, and Bubbling (up from the target back up through its parent ancestors).\n\nEvent Delegation leverages bubbling by attaching a single event listener to a shared parent container rather than individual child elements. When an event bubbles up, `event.target` identifies the specific child clicked. This saves memory and automatically handles dynamically inserted child elements without re-binding listeners."
    },
    {
        "id": "web_tech_beg_5",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "HTTP & APIs",
        "question": "What are RESTful APIs and common HTTP methods (GET, POST, PUT, DELETE)? What is the difference between 200, 400, 404, and 500 status codes?",
        "keywords": ["rest", "get", "post", "put", "delete", "status code", "200", "400", "404", "500", "idempotent", "stateless"],
        "ideal_concepts": ["REST is an architectural style based on stateless client-server communication", "GET retrieves, POST creates, PUT replaces/updates, DELETE removes", "200 OK, 400 Bad Request, 404 Not Found, 500 Internal Server Error"],
        "sample_answer": "REST (Representational State Transfer) is an architectural style for networked applications using standard HTTP protocols. Core methods include:\n- GET: Safe, idempotent retrieval of data.\n- POST: Creates a new resource.\n- PUT: Replaces/updates an entire resource.\n- DELETE: Removes a resource.\n\nHTTP status codes indicate request outcomes:\n- 200 OK: Successful request.\n- 400 Bad Request: Client sent invalid syntax or payload.\n- 404 Not Found: Resource does not exist.\n- 500 Internal Server Error: Server crashed or encountered an unexpected exception."
    },

    # Intermediate
    {
        "id": "web_tech_int_1",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Async JavaScript",
        "question": "Explain the JavaScript Event Loop, Call Stack, Microtask Queue (Promises), and Macrotask Queue (setTimeout).",
        "keywords": ["event loop", "call stack", "microtask", "macrotask", "task queue", "promise", "settimeout", "single-threaded", "non-blocking"],
        "ideal_concepts": ["JavaScript is single-threaded with a non-blocking event loop", "Call stack executes synchronous code", "Microtasks (Promise callbacks, queueMicrotask) have higher priority", "Macrotasks (setTimeout, setInterval, I/O) run after microtask queue is exhausted"],
        "sample_answer": "JavaScript is single-threaded with a call stack that executes synchronous code. Asynchronous operations are delegated to browser Web APIs.\n\nWhen asynchronous operations complete, their callbacks enter specific queues:\n1. Microtask Queue: Handles Promise callbacks (`.then()`, `async/await`) and `queueMicrotask()`. Microtasks have highest priority.\n2. Macrotask Queue: Handles timers (`setTimeout`, `setInterval`) and UI rendering events.\n\nThe Event Loop monitors the call stack. Once the call stack is completely empty, it flushes the ENTIRE Microtask Queue before picking a single task from the Macrotask Queue."
    },
    {
        "id": "web_tech_int_2",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Frontend Frameworks",
        "question": "How does the Virtual DOM work in modern frontend libraries like React, and how does Reconciliation optimize rendering?",
        "keywords": ["virtual dom", "reconciliation", "diffing", "react", "state", "props", "fiber", "repaint", "reflow", "keys"],
        "ideal_concepts": ["Virtual DOM is an in-memory lightweight JavaScript representation of real DOM", "State change creates a new VDOM tree", "Diffing algorithm compares old vs new VDOM", "Reconciliation batches and applies only necessary changes to real DOM to avoid expensive layout thrashing"],
        "sample_answer": "The real browser DOM is slow to update because direct mutations trigger layout calculation (reflow) and repainting. The Virtual DOM (VDOM) is a lightweight JavaScript object tree mirroring the actual DOM.\n\nWhen component state or props change, React creates a new VDOM tree and runs a diffing algorithm (Reconciliation) comparing it against the previous snapshot. It determines the minimum number of mutations required (e.g., using element keys to track moved list items) and batches these updates into a single efficient real DOM mutation, ensuring 60fps UI performance."
    },
    {
        "id": "web_tech_int_3",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Web Security",
        "question": "Explain CORS, XSS (Cross-Site Scripting), and CSRF (Cross-Site Request Forgery). How do you protect a web app against them?",
        "keywords": ["cors", "xss", "csrf", "security", "same-origin", "sanitization", "samesite", "jwt", "tokens", "content security policy"],
        "ideal_concepts": ["CORS relaxes Same-Origin Policy via Access-Control-Allow-Origin headers", "XSS injects malicious client-side scripts, prevented by input sanitization and CSP", "CSRF tricks authenticated users into submitting unauthorized requests, prevented by Anti-CSRF tokens and SameSite cookies"],
        "sample_answer": "- CORS (Cross-Origin Resource Sharing): A browser security mechanism that restricts HTTP requests initiated from scripts across origins unless the server responds with matching `Access-Control-Allow-Origin` headers.\n- XSS (Cross-Site Scripting): An attacker injects malicious scripts into pages viewed by other users. Mitigation: Sanitize/escape all user inputs, use modern framework templating that auto-escapes, and implement a strict Content Security Policy (CSP).\n- CSRF (Cross-Site Request Forgery): An attacker deceives an authenticated browser into sending forged requests to a trusted site. Mitigation: Use anti-CSRF tokens, verify Origin/Referer headers, and configure cookies with `SameSite=Lax` or `Strict`."
    },
    {
        "id": "web_tech_int_4",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Web Performance",
        "question": "What are Core Web Vitals (LCP, INP, CLS), and what techniques do you use to optimize page load and responsiveness?",
        "keywords": ["core web vitals", "lcp", "inp", "cls", "lazy loading", "code splitting", "bundler", "caching", "critical css", "cdn"],
        "ideal_concepts": ["LCP (Largest Contentful Paint) measures loading speed", "INP (Interaction to Next Paint) measures responsiveness", "CLS (Cumulative Layout Shift) measures visual stability", "Optimizations: Code splitting, lazy loading images/components, caching headers, minification"],
        "sample_answer": "Core Web Vitals are Google's key metrics for user experience:\n1. LCP (Largest Contentful Paint): Loading performance; main content must render within 2.5s. Optimized via CDN caching, image compression (WebP/AVIF), and preloading critical assets.\n2. INP (Interaction to Next Paint): Page responsiveness to user taps/clicks (target < 200ms). Optimized by yielding heavy JavaScript tasks to the main thread and debouncing inputs.\n3. CLS (Cumulative Layout Shift): Visual stability (target < 0.1). Optimized by setting explicit width/height dimensions on images, iframes, and reserving space for ads/dynamic elements."
    },
    {
        "id": "web_tech_int_5",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "State Management",
        "question": "How do you manage client-side state across a complex web application? Compare local component state, Context API, and global stores like Redux or Zustand.",
        "keywords": ["state management", "context api", "redux", "zustand", "props drilling", "global state", "immutability", "re-render"],
        "ideal_concepts": ["Local state (useState) handles UI component behavior", "Prop drilling happens when passing state through many layers", "Context API shares state without prop drilling but can cause unnecessary re-renders", "Redux/Zustand offer predictable central state, selective subscriptions, and devtools debugging"],
        "sample_answer": "For localized UI states (like modal toggles or form inputs), component-level state (`useState`) is simplest and fastest. When state needs to be shared down a component tree without tedious 'prop drilling', React's Context API provides a lightweight native solution, though care must be taken as changes to context cause all consuming components to re-render.\n\nFor complex, high-velocity global state (like user auth, shopping cart, or caching API data), centralized state libraries like Zustand or Redux Toolkit are superior: they use selective subscriptions (preventing unnecessary re-renders), enforce unidirectional data flow, and offer time-travel debugging."
    },

    # Advanced
    {
        "id": "web_tech_adv_1",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "SSR & Architecture",
        "question": "Explain Server-Side Rendering (SSR), Static Site Generation (SSG), Incremental Static Regeneration (ISR), and Client-Side Rendering (CSR). When do you choose each?",
        "keywords": ["ssr", "ssg", "isr", "csr", "hydration", "next.js", "seo", "time to first byte", "ttfb", "first contentful paint"],
        "ideal_concepts": ["CSR renders in browser via JS bundle (slower initial paint, bad for SEO)", "SSR renders HTML on server per request (great for dynamic, personalized data)", "SSG pre-builds HTML at build time (fastest TTFB, ideal for blogs/marketing)", "ISR updates static pages incrementally in the background without full redeploy"],
        "sample_answer": "- CSR: Browser downloads empty HTML and heavy JS bundle; renders everything client-side. Best for private dashboards/internal tools where SEO is irrelevant.\n- SSR: Server generates HTML dynamically on every HTTP request. Best for highly dynamic, user-personalized feeds needing immediate SEO and fresh data.\n- SSG: HTML is pre-rendered at build time and served via global CDN edge caches. Delivers lowest TTFB and maximum reliability; ideal for marketing pages and documentation.\n- ISR: Hybrid SSG that regenerates static pages in the background on cache expiration (stale-while-revalidate), giving static CDN speeds for millions of dynamic e-commerce product pages without full rebuilds."
    },
    {
        "id": "web_tech_adv_2",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Frontend Performance & Hydration",
        "question": "What is Hydration in modern web frameworks, why does Hydration mismatch occur, and how do Islands Architecture or React Server Components solve it?",
        "keywords": ["hydration", "react server components", "rsc", "islands architecture", "astro", "bundle size", "mismatch", "streaming"],
        "ideal_concepts": ["Hydration is the process of attaching event listeners and React state to server-rendered HTML", "Hydration mismatches occur when server HTML diverges from initial client render", "Hydration is expensive because entire JS bundle must download and execute before page is interactive", "Islands Architecture and RSC only send JS for interactive components, leaving static parts zero-JS"],
        "sample_answer": "Hydration is the client-side process where a JavaScript framework reads pre-rendered server HTML, builds the virtual tree, and attaches event listeners to make buttons clickable. A hydration mismatch occurs when the server-rendered DOM does not match the client's initial render (e.g., mismatched timestamps, random IDs, or localStorage checks).\n\nTraditional full-page hydration forces downloading megabytes of JavaScript even for static text. Modern solutions like Islands Architecture (Astro) and React Server Components (RSC) separate static content from interactive widgets: static HTML remains zero-JS, while only isolated 'interactive islands' hydrate on demand, slashing initial bundle size and time-to-interactive."
    },
    {
        "id": "web_tech_adv_3",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Web Security & Identity",
        "question": "How do you design a secure authentication and session architecture in modern Single Page Applications (SPAs)? Contrast JWT in localStorage vs HttpOnly Cookies.",
        "keywords": ["authentication", "jwt", "httponly", "cookies", "localstorage", "xss", "csrf", "refresh token", "access token", "oauth2"],
        "ideal_concepts": ["Storing JWT in localStorage makes it vulnerable to XSS exfiltration", "HttpOnly, Secure, SameSite cookies prevent JavaScript access and mitigate XSS", "Combine short-lived access tokens with rotating refresh tokens stored in HttpOnly cookies", "Mitigate CSRF with SameSite cookie attributes"],
        "sample_answer": "Storing access tokens in `localStorage` or `sessionStorage` is insecure because any Cross-Site Scripting (XSS) vulnerability allows malicious scripts to steal the token and impersonate the user.\n\nThe industry-standard architecture uses a two-token model:\n1. Short-lived Access Token (e.g., 5-15 min lifespan) held strictly in memory (JavaScript variable or React state).\n2. Long-lived Refresh Token stored inside an `HttpOnly`, `Secure`, `SameSite=Strict/Lax` cookie with an explicit path restriction (e.g., `/api/auth/refresh`).\nBecause `HttpOnly` cookies are inaccessible to JavaScript, XSS scripts cannot exfiltrate the credential, and the `SameSite` attribute safeguards against CSRF."
    },
    {
        "id": "web_tech_adv_4",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Browser Capabilities & Real-Time",
        "question": "How do WebSockets, Server-Sent Events (SSE), and HTTP Long Polling compare for real-time bidirectional communication? How do Service Workers enable offline-first apps?",
        "keywords": ["websockets", "sse", "server-sent events", "long polling", "service worker", "pwa", "offline", "cache api", "bidirectional"],
        "ideal_concepts": ["WebSockets provide full-duplex bidirectional TCP communication", "SSE provides unidirectional server-to-client streaming over HTTP/2", "Long polling is high overhead fallback", "Service Workers act as client-side network proxies intercepting requests and managing Cache API for offline capabilities"],
        "sample_answer": "For real-time data:\n- WebSockets: Full-duplex bidirectional communication over a single TCP connection; optimal for multiplayer games, collaborative editors, and instant chat.\n- Server-Sent Events (SSE): Lightweight unidirectional server-to-client streaming over standard HTTP; ideal for stock tickers, notification feeds, and LLM chat token streaming.\n- Long Polling: Legacy fallback keeping HTTP requests open until data arrives; high overhead.\n\nService Workers run on a background thread independent of web pages, acting as programmable network proxies. By intercepting `fetch` events and caching assets/API responses via the Cache API and IndexedDB, they enable Progressive Web Apps (PWAs) to run completely offline with background synchronization."
    },
    {
        "id": "web_tech_adv_5",
        "role": "Web Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Build Tooling & Bundling",
        "question": "How do modern build tools like Vite and esbuild achieve sub-second hot module replacement compared to traditional Webpack bundlers? Explain Tree Shaking.",
        "keywords": ["vite", "esbuild", "webpack", "hmr", "tree shaking", "esm", "dead code elimination", "ast", "rollup"],
        "ideal_concepts": ["Webpack bundles entire dependency graph before serving dev server", "Vite leverages native browser ES Modules (ESM) to serve unbundled code on demand", "esbuild compiles Go code with high concurrency", "Tree shaking eliminates dead code by analyzing static ES module import/export statements"],
        "sample_answer": "Traditional bundlers like Webpack crawl and bundle the entire dependency graph into memory before starting the dev server, which scales poorly as projects grow. Vite revolutionizes dev performance by serving source code over native browser ES Modules (ESM): the browser requests individual files on demand, and third-party dependencies are pre-bundled once using 'esbuild' (written in Go, running 10-100x faster than JS bundlers).\n\nTree Shaking is dead-code elimination that removes unused exports from production bundles. It relies on the static nature of ES module syntax (`import`/`export`), enabling AST parsers to determine exactly which code paths are executed and discarding unreferenced functions."
    },

    # =========================================================================
    # SOFTWARE DEVELOPER - TECHNICAL
    # =========================================================================
    # Beginner
    {
        "id": "swe_tech_beg_1",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Data Structures & Algorithms",
        "question": "What is Big-O notation, and why is it important in software development? Give the time complexity of searching an element in an unsorted array vs a binary search tree.",
        "keywords": ["big-o", "time complexity", "space complexity", "linear", "logarithmic", "o(n)", "o(log n)", "binary search", "array"],
        "ideal_concepts": ["Big-O classifies algorithm scalability as input size grows", "Worst-case vs average-case", "Linear search in unsorted array is O(n)", "Binary search in sorted array/balanced BST is O(log n)"],
        "sample_answer": "Big-O notation describes the upper bound of an algorithm's runtime or memory usage as the input size (n) scales toward infinity, allowing developers to compare performance independently of hardware.\n\nSearching an element in an unsorted array requires checking every element sequentially in the worst case, yielding O(n) linear time complexity. In contrast, searching in a sorted array or balanced Binary Search Tree halves the search space at each step, yielding O(log n) logarithmic time complexity."
    },
    {
        "id": "swe_tech_beg_2",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Software Engineering Principles",
        "question": "What are Git and version control? Explain the difference between 'git merge' and 'git rebase', and how you handle merge conflicts.",
        "keywords": ["git", "version control", "merge", "rebase", "conflict", "commit", "branch", "history", "pull request"],
        "ideal_concepts": ["Git is a distributed version control system tracking source code history", "git merge preserves true chronological history with a merge commit", "git rebase creates a clean linear history by replaying commits", "Merge conflicts occur when changes overlap and require manual resolution"],
        "sample_answer": "Git is a distributed version control system tracking changes across collaborative codebases. 'git merge' combines branches by creating a dedicated merge commit, preserving the exact historical timeline of feature branches. In contrast, 'git rebase' takes commits from your branch and replays them on top of the target base branch, creating a clean, linear commit history.\n\nWhen a merge conflict occurs, Git marks the conflicting lines between `<<<<<<<` and `>>>>>>>`. I resolve it by discussing with team members, selecting the correct code, staging the resolved file with `git add`, and finishing the commit."
    },
    {
        "id": "swe_tech_beg_3",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Databases",
        "question": "What is the difference between SQL (relational) and NoSQL (non-relational) databases? When would you choose PostgreSQL vs MongoDB?",
        "keywords": ["sql", "nosql", "relational", "schema", "acid", "postgresql", "mongodb", "documents", "foreign key", "scalability"],
        "ideal_concepts": ["SQL databases have rigid schemas, tables, relationships, and ACID compliance", "NoSQL databases are schema-flexible (documents, key-value, graph, columnar)", "Choose PostgreSQL for structured data, complex joins, financial integrity", "Choose MongoDB for rapid schema prototyping, nested documents, unstructured data"],
        "sample_answer": "SQL databases (like PostgreSQL, MySQL) are relational, use structured schemas with tables, rows, and foreign keys, and strictly adhere to ACID transactions. NoSQL databases (like MongoDB, Cassandra) are document, key-value, or graph-oriented, offering flexible schemas and horizontal scalability.\n\nI would choose PostgreSQL when data relationships are complex, integrity is paramount (e.g., payments, user accounts, transactional ledgers), and complex multi-table joins are needed. I would choose MongoDB for rapid prototyping, polymorphic data models, or document-centric catalogs where data schema changes frequently."
    },
    {
        "id": "swe_tech_beg_4",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Software Architecture / Clean Code",
        "question": "What does the DRY (Don't Repeat Yourself) principle mean, and why should code maintainability take priority over clever one-liners?",
        "keywords": ["dry", "maintainability", "readability", "refactoring", "technical debt", "abstraction", "modular", "clean code"],
        "ideal_concepts": ["DRY reduces duplication and centralizes business logic", "Clever one-liners are hard to read, debug, and test", "Code is read far more often than it is written"],
        "sample_answer": "The DRY (Don't Repeat Yourself) principle states that every piece of domain knowledge or logic must have a single, unambiguous representation within a system. Duplicating logic means bugs must be fixed in multiple places, leading to regressions and technical debt.\n\nCode maintainability and readability must always take priority over clever one-liners. Software is read and maintained dozens of times more than it is written. Clean, modular code with clear naming and descriptive functions enables teammates to debug, test, and onboard seamlessly without misunderstanding."
    },
    {
        "id": "swe_tech_beg_5",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Testing & Quality Assurance",
        "question": "What is the difference between Unit Testing, Integration Testing, and End-to-End (E2E) Testing? What is the Testing Pyramid?",
        "keywords": ["unit testing", "integration testing", "e2e", "end to end", "testing pyramid", "mock", "regression", "qa", "pytest", "jest"],
        "ideal_concepts": ["Unit tests isolate single functions using mocks (fast, cheap)", "Integration tests verify communication between modules/databases", "E2E tests simulate real user journeys in a browser (slow, fragile)", "Testing Pyramid emphasizes many unit tests, moderate integration tests, few E2E tests"],
        "sample_answer": "- Unit Testing: Tests individual functions or classes in complete isolation by mocking external dependencies; fast and inexpensive to run.\n- Integration Testing: Tests the interaction between integrated units, such as a backend service communicating with a database or third-party API.\n- End-to-End (E2E) Testing: Simulates the entire user journey through the live system from UI to backend.\n\nThe Testing Pyramid advocates for a large foundation of fast, automated unit tests, a middle layer of integration tests, and a small apex of high-value E2E tests, balancing test speed, cost, and confidence."
    },

    # Intermediate
    {
        "id": "swe_tech_int_1",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Design Patterns",
        "question": "Explain three common software design patterns (e.g., Singleton, Factory, and Observer). Describe a real-world scenario where you would use one.",
        "keywords": ["design pattern", "singleton", "factory", "observer", "solid", "creational", "behavioral", "event", "instance"],
        "ideal_concepts": ["Singleton ensures only one instance exists (e.g., database connection pool)", "Factory decouples object creation from business logic", "Observer defines one-to-many subscription model for event-driven systems"],
        "sample_answer": "1. Singleton (Creational): Ensures a class has only one global instance and provides a global access point. Used for centralized resources like logging systems or database connection pools.\n2. Factory Method (Creational): Delegates object instantiation to subclasses or specialized methods based on input parameters, decoupling client code from concrete implementations (e.g., generating PaymentProcessors for Stripe vs PayPal).\n3. Observer (Behavioral): Defines a one-to-many subscription dependency where subject state changes automatically notify all registered observers.\n\nIn a real-world e-commerce app, I use the Observer pattern for order fulfillment: when an order status changes to 'PAID', observer services (NotificationService, InventoryService, InvoiceGenerator) react independently without tight coupling."
    },
    {
        "id": "swe_tech_int_2",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "System Design & Caching",
        "question": "What is caching, and how does a Cache-Aside (Lazy Loading) strategy work? What are common cache eviction policies (LRU, LFU)?",
        "keywords": ["caching", "redis", "memcached", "cache-aside", "lru", "lfu", "ttl", "stale data", "eviction", "latency"],
        "ideal_concepts": ["Caching stores frequently accessed data in fast in-memory storage (Redis)", "Cache-Aside checks cache first; on miss, reads from DB and populates cache", "LRU (Least Recently Used) evicts items not accessed recently", "Cache invalidation strategies (TTL, write-through)"],
        "sample_answer": "Caching stores high-demand computation or database results in fast in-memory storage (like Redis or Memcached) to reduce latency and database load.\n\nIn the Cache-Aside (Lazy Loading) pattern, the application first queries the cache. If a cache hit occurs, data is returned instantly. On a cache miss, the application queries the persistent database, writes the result to the cache for future requests, and returns it to the client.\n\nWhen memory is full, eviction policies reclaim space: LRU (Least Recently Used) discards the item that hasn't been accessed for the longest time, while LFU (Least Frequently Used) discards items with the lowest access count."
    },
    {
        "id": "swe_tech_int_3",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "SOLID Principles",
        "question": "Explain the SOLID principles of Object-Oriented Design. Pick two principles and provide examples of how violating them causes technical debt.",
        "keywords": ["solid", "single responsibility", "open closed", "liskov substitution", "interface segregation", "dependency inversion", "refactoring"],
        "ideal_concepts": ["S: Single Responsibility, O: Open-Closed, L: Liskov Substitution, I: Interface Segregation, D: Dependency Inversion", "Violating Single Responsibility creates 'God classes' that break on any edit", "Violating Open-Closed requires modifying existing tested code to add new features"],
        "sample_answer": "SOLID stands for:\n- S: Single Responsibility Principle (a class should have one reason to change).\n- O: Open/Closed Principle (open for extension, closed for modification).\n- L: Liskov Substitution Principle (subtypes must be substitutable for base types).\n- I: Interface Segregation Principle (clients shouldn't depend on interfaces they don't use).\n- D: Dependency Inversion Principle (depend on abstractions, not concretions).\n\nFor example, violating Single Responsibility by putting user authentication, email sending, and database persistence in one 'UserManager' class means changes to email styling risk breaking authentication logic. Violating Open-Closed by using long switch-statements to handle payment types means adding 'Apple Pay' requires editing and re-testing core payment code rather than simply implementing a new PaymentStrategy interface."
    },
    {
        "id": "swe_tech_int_4",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Databases & Transactions",
        "question": "What are ACID properties in database management? What is database indexing, and why shouldn't every column be indexed?",
        "keywords": ["acid", "atomicity", "consistency", "isolation", "durability", "b-tree", "index", "write overhead", "storage", "performance"],
        "ideal_concepts": ["Atomicity: all-or-nothing", "Consistency: valid database state", "Isolation: concurrent transactions don't interfere", "Durability: committed data survives crashes", "B-Tree indexing accelerates lookups from O(n) to O(log n)", "Drawback: Indexes add write overhead (inserts/updates/deletes) and consume storage"],
        "sample_answer": "ACID properties ensure reliable database transactions:\n- Atomicity: An entire transaction completes, or all changes roll back (all-or-nothing).\n- Consistency: Transactions transition the database from one valid state to another, respecting all constraints.\n- Isolation: Concurrent transactions execute without interfering with one another.\n- Durability: Committed transactions survive system crashes.\n\nDatabase indexing (typically using B-Trees) drastically accelerates query lookups from O(n) full table scans to O(log n) tree traversals. However, indexing every column harms performance because every INSERT, UPDATE, and DELETE must rebalance and write to all corresponding indexes, slowing writes and consuming excessive storage."
    },
    {
        "id": "swe_tech_int_5",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "DevOps & CI/CD",
        "question": "What is Continuous Integration and Continuous Deployment (CI/CD)? Describe the typical stages in a modern automated pipeline.",
        "keywords": ["ci/cd", "continuous integration", "continuous deployment", "pipeline", "docker", "automated testing", "linting", "staging", "production"],
        "ideal_concepts": ["CI regularly merges developer code branches and validates them with automated builds and tests", "CD automatically delivers or deploys tested artifacts to staging/production", "Pipeline stages: Checkout -> Lint/Static Analysis -> Unit/Integration Tests -> Build/Containerize -> Deploy"],
        "sample_answer": "Continuous Integration (CI) is the practice where developers frequently merge code changes into a central repository, triggering automated builds, linters, and test suites to catch bugs immediately. Continuous Deployment (CD) automatically releases validated code into production environments without manual intervention.\n\nA typical pipeline sequence consists of:\n1. Source/Trigger: Triggered upon pull request or push to main branch.\n2. Linting & Static Code Analysis: Verifies style standards and security vulnerabilities.\n3. Automated Testing: Executes unit and integration test suites.\n4. Build & Package: Compiles code and builds an immutable Docker container image.\n5. Deploy: Deploys to staging for smoke testing, followed by rolling deployment to production."
    },

    # Advanced
    {
        "id": "swe_tech_adv_1",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Distributed Systems",
        "question": "Explain the CAP Theorem and PACELC theorem. How do you choose between Consistency and Availability in a globally distributed system?",
        "keywords": ["cap theorem", "pacelc", "consistency", "availability", "partition tolerance", "network partition", "latency", "distributed systems"],
        "ideal_concepts": ["CAP: In presence of network partition (P), you must choose between Consistency (C) or Availability (A)", "PACELC: If Partition (P), choose Availability (A) or Consistency (C); Else (E), choose Latency (L) or Consistency (C)", "CP systems: reject requests if quorum cannot be reached", "AP systems: accept writes and reconcile later (eventual consistency)"],
        "sample_answer": "The CAP Theorem states that in any distributed data store, network partitions (P) are unavoidable; thus, during a partition, the system must choose between Consistency (C - every read receives the most recent write or an error) and Availability (A - every non-failing node returns a response, but it may be stale).\n\nThe PACELC theorem extends CAP: if there is a Partition (P), choose between Availability (A) and Consistency (C); Else (E), when the network is normal, choose between Latency (L) and Consistency (C).\n\nFor banking, financial ledgers, or inventory reservation, I choose CP (using Raft/Paxos quorums like CockroachDB), sacrificing availability to avoid corrupt state. For social media feeds, metrics, or streaming views, I choose AP (like Cassandra/DynamoDB), favoring high availability and low latency with eventual consistency."
    },
    {
        "id": "swe_tech_adv_2",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Scalability & Resilience",
        "question": "How do you design a resilient system that prevents cascading failures? Explain Circuit Breakers, Bulkheads, Rate Limiting, and Idempotency.",
        "keywords": ["circuit breaker", "bulkhead", "rate limiting", "idempotency", "cascading failure", "token bucket", "resilience", "timeout", "retry"],
        "ideal_concepts": ["Circuit Breakers trip to open state when failure threshold is exceeded to protect downstream services", "Bulkheads isolate resource pools so one tenant or failure doesn't exhaust shared resources", "Rate limiting protects against traffic spikes (Token Bucket / Leaky Bucket)", "Idempotency keys ensure retrying network requests doesn't duplicate transactions"],
        "sample_answer": "Cascading failures occur when one failing downstream dependency backs up requests and causes upstream services to exhaust memory and threads.\n\nTo prevent this:\n1. Circuit Breakers (e.g., Resilience4j): Monitor failure rates. When errors exceed a threshold, the breaker trips to 'Open', immediately failing fast without burdening the struggling service, giving it room to recover.\n2. Bulkheads: Segregate thread pools and memory quotas so an outage in one domain doesn't consume all system resources.\n3. Rate Limiting: Algorithms like Token Bucket or Sliding Window log reject excessive traffic to maintain SLA guarantees.\n4. Idempotency: Clients send unique idempotency keys in headers; if an HTTP request times out and retries, the server recognizes the key and avoids duplicating critical actions like credit card charges."
    },
    {
        "id": "swe_tech_adv_3",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Database Architecture & Sharding",
        "question": "How do you scale a relational database handling terabytes of data? Explain Vertical vs Horizontal Partitioning, Sharding, and Consistent Hashing.",
        "keywords": ["sharding", "partitioning", "consistent hashing", "database scaling", "read replica", "shard key", "rebalancing", "virtual nodes"],
        "ideal_concepts": ["Read replicas offload read traffic", "Vertical partitioning splits tables by columns or domains", "Horizontal partitioning/sharding splits rows across multiple database instances", "Consistent Hashing minimizes data movement when adding or removing shards"],
        "sample_answer": "Scaling relational databases begins with Read Replicas to offload read-heavy queries. When write throughput or dataset size exceeds a single master's disk and RAM limits, sharding is required.\n\nHorizontal Sharding distributes rows across independent database servers based on a shard key (e.g., user_id or organization_id). Choosing the right shard key is critical to avoid hot spots and cross-shard queries.\n\nConsistent Hashing arranges shards in an abstract logical ring. Hash values map keys to the next available node on the ring. When adding or removing database nodes, only k/N keys need to be migrated rather than rehashing the entire database, preventing system-wide downtime during cluster resizing."
    },
    {
        "id": "swe_tech_adv_4",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Event-Driven Architecture",
        "question": "Compare message queues (RabbitMQ) vs distributed event logs (Apache Kafka). When would you use Event Sourcing and CQRS?",
        "keywords": ["kafka", "rabbitmq", "message queue", "event log", "cqrs", "event sourcing", "pub/sub", "backpressure", "offset", "replay"],
        "ideal_concepts": ["RabbitMQ is a smart broker/dumb consumer queue that deletes messages after ACK", "Kafka is a dumb broker/smart consumer partitioned commit log that persists messages and allows replaying", "Event Sourcing records state as an immutable sequence of events", "CQRS separates Read model from Write model for optimized querying"],
        "sample_answer": "RabbitMQ is an AMQP message broker where the broker manages message routing, delivery guarantees, and deletes messages once acknowledged by consumers; it excels at complex point-to-point routing and background worker queues. Kafka is a distributed, append-only commit log where consumers manage their own read offsets and messages are retained for days or months, allowing message replay and massive stream processing throughput.\n\nEvent Sourcing stores every state mutation as an append-only historical event (e.g., 'ItemAddedToCart', 'PaymentCaptured') rather than updating current row state. When paired with CQRS (Command Query Responsibility Segregation), commands write to the event log while optimized read models (like Elasticsearch or materialized views) handle fast, denormalized read queries."
    },
    {
        "id": "swe_tech_adv_5",
        "role": "Software Developer",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "Security & Cryptography",
        "question": "How does asymmetric cryptography (Public/Private keys) differ from symmetric cryptography? How does TLS/HTTPS establish a secure session?",
        "keywords": ["cryptography", "symmetric", "asymmetric", "aes", "rsa", "tls", "https", "handshake", "certificate authority", "diffie-hellman"],
        "ideal_concepts": ["Symmetric uses same key for encryption/decryption (fast, AES)", "Asymmetric uses public key for encryption and private key for decryption (slower, RSA/ECC)", "TLS Handshake uses asymmetric encryption / Diffie-Hellman to authenticate server and exchange ephemeral symmetric session keys", "Symmetric session key encrypts actual HTTP payload"],
        "sample_answer": "Symmetric encryption (e.g., AES-256) uses a single secret key for both encryption and decryption; it is computationally fast and ideal for encrypting large payloads. Asymmetric encryption (e.g., RSA, Elliptic Curve) uses a mathematically linked key pair: the public key encrypts, and only the private key decrypts.\n\nThe TLS 1.3 handshake combines both strengths:\n1. The client sends supported cipher suites.\n2. The server presents its digital certificate issued by a trusted Certificate Authority (CA) to prove its identity.\n3. Using asymmetric key exchange (like Ephemeral Diffie-Hellman), the client and server negotiate a shared secret without ever transmitting the key over the wire.\n4. All subsequent HTTP traffic is encrypted using high-speed symmetric session keys derived from that shared secret."
    },

    # =========================================================================
    # OTHER / GENERAL CS - TECHNICAL
    # =========================================================================
    # Beginner
    {
        "id": "other_tech_beg_1",
        "role": "Other",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Computer Science Core",
        "question": "What is the difference between a process and a thread in an operating system? How does context switching work?",
        "keywords": ["process", "thread", "operating system", "memory space", "context switch", "pcb", "registers", "multitasking"],
        "ideal_concepts": ["Process has its own isolated address space and resources", "Threads belong to a process and share memory and code segment", "Context switching saves and restores CPU register states"],
        "sample_answer": "A process is an executing program instance with its own independent, protected address space, memory, and resources allocated by the operating system. A thread is the smallest unit of CPU execution within a process, sharing the parent process's memory space, open file descriptors, and code segment, while maintaining its own program counter and stack.\n\nContext switching is the OS mechanism of pausing one process/thread, saving its CPU register states and program counter into a Process Control Block (PCB), and loading the saved state of another ready process into CPU registers to enable multitasking."
    },
    {
        "id": "other_tech_beg_2",
        "role": "Other",
        "type": "Technical",
        "difficulty": "Beginner",
        "category": "Networking",
        "question": "What is the difference between TCP and UDP? Give an example application where each protocol is appropriate.",
        "keywords": ["tcp", "udp", "connection-oriented", "connectionless", "handshake", "packet", "reliability", "latency", "streaming", "http"],
        "ideal_concepts": ["TCP is connection-oriented, reliable, guarantees order via 3-way handshake and ACK", "UDP is connectionless, lightweight, no delivery guarantee or retransmission", "TCP used for web pages, file transfers, emails", "UDP used for live video streaming, voice calls (VoIP), online gaming"],
        "sample_answer": "TCP (Transmission Control Protocol) is a connection-oriented protocol that establishes a connection via a 3-way handshake (SYN, SYN-ACK, ACK), guarantees reliable delivery, error checking, and packet sequencing. It is used where accuracy is critical, such as HTTP/HTTPS web browsing, file downloads (FTP), and banking systems.\n\nUDP (User Datagram Protocol) is a lightweight, connectionless protocol that transmits packets without handshakes or retransmission guarantees. It minimizes latency and packet overhead, making it ideal for real-time video streaming, VoIP calls, and competitive multiplayer games where dropping an occasional packet is preferable to buffering."
    },

    # Intermediate
    {
        "id": "other_tech_int_1",
        "role": "Other",
        "type": "Technical",
        "difficulty": "Intermediate",
        "category": "Operating Systems & Concurrency",
        "question": "What is a deadlock in an operating system? What are the four Coffman conditions required for a deadlock to occur, and how can they be prevented?",
        "keywords": ["deadlock", "coffman conditions", "mutual exclusion", "hold and wait", "no preemption", "circular wait", "banker's algorithm"],
        "ideal_concepts": ["Deadlock occurs when processes are blocked waiting for resources held by each other", "Coffman conditions: Mutual Exclusion, Hold and Wait, No Preemption, Circular Wait", "Breaking any single condition prevents deadlock"],
        "sample_answer": "A deadlock occurs when two or more processes are permanently blocked because each holds a resource that the other requires to proceed.\n\nThe four necessary Coffman conditions are:\n1. Mutual Exclusion: At least one resource is held in a non-shareable mode.\n2. Hold and Wait: A process holds one resource while requesting additional resources.\n3. No Preemption: Resources cannot be forcibly taken from a process until released.\n4. Circular Wait: A closed chain of processes exists where each waits for a resource held by the next.\n\nDeadlock can be prevented by invalidating any of these conditions, most commonly eliminating Circular Wait by enforcing a strict global ordering on resource acquisition."
    },

    # Advanced
    {
        "id": "other_tech_adv_1",
        "role": "Other",
        "type": "Technical",
        "difficulty": "Advanced",
        "category": "System Architecture",
        "question": "Explain how an API Gateway functions in a modern cloud architecture. What responsibilities does it offload from backend microservices?",
        "keywords": ["api gateway", "reverse proxy", "rate limiting", "authentication", "load balancing", "ssl termination", "routing", "bff"],
        "ideal_concepts": ["API Gateway serves as the single reverse proxy entry point for client traffic", "Offloads cross-cutting concerns: SSL termination, OAuth/JWT verification, rate limiting, request logging", "Provides request routing and response aggregation (Backend-for-Frontend / BFF pattern)"],
        "sample_answer": "An API Gateway acts as the single entry point and reverse proxy for all external client requests in a microservices ecosystem. Instead of exposing dozens of microservices directly, clients communicate with the Gateway.\n\nIt offloads critical cross-cutting concerns from individual services:\n1. Authentication & Authorization: Validates JWTs or API keys before traffic reaches microservices.\n2. SSL/TLS Termination: Decrypts HTTPS traffic at the perimeter.\n3. Rate Limiting & Throttling: Protects internal services from DDoS and abuse.\n4. Routing & Protocol Translation: Routes requests to internal microservices and converts HTTP/REST into gRPC.\n5. Caching and Metrics: Collects distributed tracing spans and access logs centrally."
    },

    # =========================================================================
    # HR / BEHAVIORAL QUESTIONS (Common across all roles, with tailored STAR answers)
    # =========================================================================
    # Beginner
    {
        "id": "hr_beg_1",
        "role": "Any",
        "type": "HR",
        "difficulty": "Beginner",
        "category": "Self Introduction & Motivation",
        "question": "Tell me about yourself, your academic background in Computer Engineering, and why you are interested in this specific role.",
        "keywords": ["background", "computer engineering", "projects", "passion", "skills", "growth", "interest", "technology", "career"],
        "ideal_concepts": ["Structured answer (Past, Present, Future)", "Academic foundation and hands-on projects", "Clear connection between skills and the target role"],
        "sample_answer": "I am a third-year Computer Engineering student passionate about building scalable, user-centric software applications. Throughout my degree, I have developed a strong foundation in data structures, algorithms, and full-stack development, while actively collaborating on practical team projects like a full-stack web application.\n\nWhat excites me about this role is the opportunity to transition my academic knowledge and problem-solving skills into production-grade systems, while learning best engineering practices from an experienced development team."
    },
    {
        "id": "hr_beg_2",
        "role": "Any",
        "type": "HR",
        "difficulty": "Beginner",
        "category": "Strengths & Weaknesses",
        "question": "What would you consider your greatest technical strength, and what is one area you are actively working to improve?",
        "keywords": ["strength", "improvement", "growth mindset", "learning", "documentation", "debugging", "problem solving", "self-awareness"],
        "ideal_concepts": ["Honest, self-aware assessment", "Demonstrates actionable steps being taken to improve", "Turns weakness into an active learning journey"],
        "sample_answer": "My greatest strength is my methodical approach to debugging and root-cause analysis: when encountering unexpected errors, I reproduce the issue, read stack traces thoroughly, and systematically isolate variables rather than making guesswork changes.\n\nAn area I am actively improving is public technical communication. In early group projects, I felt hesitant to present complex architectural choices to larger audiences. To overcome this, I have started documenting my design decisions in markdown RFCs and leading sprint demos for my college project teams."
    },
    {
        "id": "hr_beg_3",
        "role": "Any",
        "type": "HR",
        "difficulty": "Beginner",
        "category": "Handling Deadlines",
        "question": "Describe a situation during your college or project work where you faced a tight deadline. How did you prioritize your tasks to deliver on time?",
        "keywords": ["deadline", "prioritization", "star method", "time management", "mvp", "communication", "milestones"],
        "ideal_concepts": ["Uses STAR framework (Situation, Task, Action, Result)", "Focuses on MVP (Minimum Viable Product)", "Proactive communication and time management"],
        "sample_answer": "During our semester database project, our four-person team had only one week remaining when our backend API integration encountered unexpected data schema conflicts (Situation). As the project lead, I needed to ensure we submitted a working, tested application by the Friday deadline (Task).\n\nI organized a quick triage meeting, decomposed our pending features into an MVP (Minimum Viable Product), prioritized core CRUD operations over optional animation polish, and set up a shared Kanban board with daily 15-minute syncs (Action). As a result, we delivered the project 12 hours ahead of the deadline with zero critical defects and received an A grade on our submission (Result)."
    },

    # Intermediate
    {
        "id": "hr_int_1",
        "role": "Any",
        "type": "HR",
        "difficulty": "Intermediate",
        "category": "Teamwork & Conflict Resolution",
        "question": "Tell me about a time when you had a technical disagreement with a teammate or project partner. How did you resolve it?",
        "keywords": ["disagreement", "conflict", "teamwork", "star", "data-driven", "compromise", "listening", "empathy", "resolution"],
        "ideal_concepts": ["STAR method", "Constructive debate focusing on technical merits and data, not ego", "Respectful compromise and alignment with project goals"],
        "sample_answer": "In our third-year group project, a teammate and I disagreed on whether to use a document-based NoSQL database or a relational PostgreSQL schema (Situation). My colleague wanted MongoDB for quick prototyping, whereas I believed our relational schema and strict transaction requirements needed PostgreSQL (Task).\n\nInstead of debating opinions, I proposed building a quick 2-hour proof-of-concept benchmark modeling our core entity relationships. We analyzed the complexity of multi-table joins and data integrity rules together (Action). Recognizing that our user and order data required foreign key constraints and ACID guarantees, my teammate agreed PostgreSQL was the right technical choice, and we collaborated smoothly on the schema design (Result)."
    },
    {
        "id": "hr_int_2",
        "role": "Any",
        "type": "HR",
        "difficulty": "Intermediate",
        "category": "Learning from Failure",
        "question": "Describe a project or technical task that did not go as planned. What was the mistake, how did you handle it, and what did you learn?",
        "keywords": ["failure", "mistake", "accountability", "ownership", "post-mortem", "learning", "growth", "recovery"],
        "ideal_concepts": ["Takes full ownership without blaming others", "Shows systematic root-cause discovery", "Details preventive measures implemented afterwards"],
        "sample_answer": "While deploying a web application for our college tech fest, I pushed a database migration script directly to production that accidentally dropped a foreign key constraint, causing user registrations to fail for about 20 minutes (Situation).\n\nI immediately notified our faculty advisor, rolled back the database to the previous automated snapshot, and restored registration availability within 15 minutes (Action). After resolving the incident, I wrote a blameless post-mortem document. I established a staging environment identical to production and created a pre-commit hook that ran schema validations before any migration script could be executed, ensuring the mistake could never reoccur (Result)."
    },

    # Advanced
    {
        "id": "hr_adv_1",
        "role": "Any",
        "type": "HR",
        "difficulty": "Advanced",
        "category": "Leadership & Ambiguity",
        "question": "Describe a situation where you had to work with ambiguous requirements or lead an initiative with minimal guidance. How did you proceed?",
        "keywords": ["ambiguity", "leadership", "initiative", "stakeholders", "rfc", "requirements", "clarification", "iteration"],
        "ideal_concepts": ["Proactively seeking clarity rather than freezing", "Drafting proposals / RFCs for alignment", "Delivering iteratively with feedback loops"],
        "sample_answer": "During an industry internship, I was tasked with 'improving the observability of the internal microservices' with no predefined metrics or architecture guidelines (Situation). My objective was to define a concrete technical strategy and deliver actionable monitoring (Task).\n\nI started by interviewing three senior engineers and our operations lead to understand their biggest pain points during past production incidents. Finding that tracking inter-service latency was the top challenge, I wrote an RFC outlining a distributed tracing plan with OpenTelemetry, presented it for peer review, and built a pilot implementation for our authentication service (Action). The initiative established standardized tracing guidelines across the team, reducing incident triage time by 40% (Result)."
    },
    {
        "id": "hr_adv_2",
        "role": "Any",
        "type": "HR",
        "difficulty": "Advanced",
        "category": "Mentorship & Engineering Culture",
        "question": "How do you approach code reviews? How do you give constructive feedback to peers without creating friction, and how do you handle critique on your own code?",
        "keywords": ["code review", "constructive feedback", "culture", "empathy", "nitpick", "learning", "humility", "standards"],
        "ideal_concepts": ["Focus on code and principles, not personal critique", "Prefixing comments (e.g. 'nit:', 'suggestion:', 'question:')", "Welcoming critique on own code as a learning opportunity"],
        "sample_answer": "I view code reviews as a collaborative learning opportunity rather than a policing exercise. When reviewing peer code, I frame comments around principles and questions rather than directives—for example, asking 'How does this handler behave if the network times out?' instead of 'You forgot a timeout'. I also clearly categorize feedback using prefixes like 'nit:' for minor style preferences vs 'blocking:' for security or race condition bugs.\n\nWhen receiving feedback on my own pull requests, I separate my identity from my code. I welcome tough critique with curiosity, test suggested alternative approaches, and thank reviewers for catching potential defects before they reach production."
    }
]


def get_questions_for_session(role: str, interview_type: str, difficulty: str, count: int = 5):
    """
    Selects 5 balanced questions for an interview session based on role, type, and difficulty.
    Ensures question variety and appropriate distribution.
    """
    normalized_role = role.strip()
    if normalized_role not in ["Java Developer", "Web Developer", "Software Developer"]:
        lookup_role = "Other"
    else:
        lookup_role = normalized_role

    tech_questions = [
        q for q in QUESTION_BANK 
        if q["type"] == "Technical" 
        and (q["role"] == lookup_role or q["role"] == "Software Developer" or q["role"] == "Other")
        and q["difficulty"] == difficulty
    ]

    # If not enough at exact difficulty, broaden difficulty
    if len(tech_questions) < count:
        tech_questions += [
            q for q in QUESTION_BANK 
            if q["type"] == "Technical" 
            and (q["role"] == lookup_role or q["role"] == "Software Developer" or q["role"] == "Other")
            and q not in tech_questions
        ]

    hr_questions = [
        q for q in QUESTION_BANK 
        if q["type"] == "HR" 
        and (q["difficulty"] == difficulty or q["difficulty"] in ["Beginner", "Intermediate", "Advanced"])
    ]

    import random

    selected = []
    if interview_type == "Technical":
        # 5 Technical questions
        pool = list(tech_questions)
        random.shuffle(pool)
        selected = pool[:count]
    elif interview_type == "HR":
        # 5 HR questions
        pool = list(hr_questions)
        random.shuffle(pool)
        selected = pool[:count]
    else:
        # Mixed: 3 Technical + 2 HR questions
        tech_pool = list(tech_questions)
        hr_pool = list(hr_questions)
        random.shuffle(tech_pool)
        random.shuffle(hr_pool)
        
        tech_picks = tech_pool[:3]
        hr_picks = hr_pool[:2]
        
        # Interleave: Tech, Tech, HR, Tech, HR
        interleaved = []
        if len(tech_picks) > 0: interleaved.append(tech_picks[0])
        if len(tech_picks) > 1: interleaved.append(tech_picks[1])
        if len(hr_picks) > 0: interleaved.append(hr_picks[0])
        if len(tech_picks) > 2: interleaved.append(tech_picks[2])
        if len(hr_picks) > 1: interleaved.append(hr_picks[1])
        
        selected = interleaved[:count]

    # Fallback safety if selected is less than count
    if len(selected) < count:
        extra_pool = [q for q in QUESTION_BANK if q not in selected]
        random.shuffle(extra_pool)
        selected += extra_pool[:(count - len(selected))]

    return selected[:count]
