
# APD Project: Parallel and Distributed Word Count Analysis

This project explores three different computational strategies to solve the **Word Count** problem using Python. The objective is to analyze the performance benefits of parallel and distributed computing over traditional sequential processing.

##  Project Structure

According to the project hierarchy, the source code is organized into specific folders for each processing paradigm:

```text
APD_PROJECT/
├── data/                       # Global data folder
└── src/                        # Source code folder
    ├── Dask/                   # Dask implementation
    │   ├── data/               # Local data for Dask tests
    │   ├── generator.py        # Script to generate the test dataset
    │   └── procesare.py        # Dask distributed processing logic
    ├── MultiProcessing/        # Multi-core implementation
    │   └── MultiProcessing.py  # Multi-processing logic
    └── Sequential/             # Single-threaded implementation
        └── sequential.py       # Baseline linear logic
```

---

##  Getting Started

### 1. Prerequisites
You need Python 3.8+ and the Dask library installed:
```bash
pip install dask distributed
```

### 2. Generate the Dataset
Before running the benchmarks, navigate to the `Dask` folder and run the generator script to create the `date_mari.txt` file:
```bash
cd src/Dask
python generator.py
```
*Note: This will generate a large text file used by all processing versions.*

### 3. Run the Benchmarks
Navigate to each folder and execute the scripts to compare performance:

**Sequential Version:**
```bash
cd src/Sequential
python sequential.py
```

**MultiProcessing Version:**
```bash
cd src/MultiProcessing
python MultiProcessing.py
```

**Dask Version:**
```bash
cd src/Dask
python procesare.py
```

---

##  Methodology

### **1. Sequential (`sequential.py`)**
The baseline approach. It processes the text file linearly on a single CPU core. It is easy to debug but cannot handle massive datasets efficiently.

### **2. MultiProcessing (`MultiProcessing.py`)**
Uses the Python `multiprocessing` library to split the text into chunks. Each chunk is processed by a separate worker (CPU core) simultaneously, bypassing the Global Interpreter Lock (GIL).

### **3. Dask (`procesare.py`)**
Implements a **MapReduce** workflow using `dask.bag`. It is designed for "Big Data" that exceeds the computer's RAM capacity. It provides a visual dashboard to monitor task execution and memory management.

---

##  Performance Comparison
*Estimated results based on a 100MB dataset on an 8-core CPU:*

| Method | Execution Time | Resource Usage | Efficiency |
| :--- | :--- | :--- | :--- |
| **Sequential** | ~12.5s | 1 Core |  Low |
| **MultiProcessing**| ~3.5s | All Cores |  High |
| **Dask** | ~4.8s | All Cores |  Scalable |

---

##  Conclusion
This project demonstrates that **parallelism** (MultiProcessing) provides the fastest local execution, while **distributed computing** (Dask) offers the best scalability for datasets that are too large to fit in memory. The **Sequential** method remains the gold standard for small, simple tasks where parallel overhead is not justified.
