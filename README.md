# **PyFileMaster**

## *A Comprehensive File Handling Utility for Python*

## **About PyFileMaster**
PyFileMaster is an open-source Python package designed to simplify file handling tasks. Created by [Shubhashish Chakraborty](https://shubhlinks.vercel.app/), this package provides a set of powerful and easy-to-use methods for handling files, including reading, writing, and converting between formats such as binary (.dat), CSV (Excel), and text files.

With PyFileMaster, file operations become seamless. Simply provide the file path, and let the library handle the heavy lifting for you — no need for extra code or complex logic!

## **Features and Functionalities (As of ![PyPI](https://img.shields.io/pypi/v/pyfilemaster))**

- **Write Binary Files (`writeBinFile`)**  
  It creates a Binary file containing Data which is being passed, *List of dictionaries to be stored in the file*:
  ```python
  import pyfilemaster as pfm

  pfm.writeBinFile("<path_name_of_your_binary_file>" , [
      {
          'name': 'Andrew',
          'language': 'python'
      },
      {
          'name': 'Tristan',
          'language': 'JavaScript'
      }
  ])

  ```

- **Read Binary Files (`readBinFile`)**  
  Effortlessly reads and prints the contents of a binary (.dat) file.
  ```python
  import pyfilemaster as pfm

  pfm.readBinFile("<path_to_your_binary_file>")
  ```

- **Convert Binary to CSV (`convertBinToCSV`)**  
  Converts data from a binary (.dat) file to a CSV (Excel) file in just one step.
  ```python
  import pyfilemaster as pfm

  pfm.convertBinToCSV("<path_to_your_binary_file>", "<name_of_the_generated_csv_file>")
  ```

## **Installation**
### *Install the Latest Version ![PyPI](https://img.shields.io/pypi/v/pyfilemaster)*
To get started with PyFileMaster, install it via `pip`:

```bash
pip install pyfilemaster
```
Alternative commands (if pip requires specific environment handling):
```bash
pip3 install pyfilemaster
sudo pip install pyfilemaster
```

## **Getting Started**

1. Install the package using the installation instructions provided above.
2. Import the package into your Python script to start using its functionalities:
   ```python
   import pyfilemaster as pfm
   ```
3. Start using the available methods like `readBinFile` or `convertBinToCSV` to handle your file operations!


## **Contributing**

We welcome contributions from the community! Here's how you can contribute:

1. Fork the repository on [GitHub](https://www.github.com/Shubhashish-Chakraborty/pyfilemaster).
2. Make your changes in a separate branch.
3. Submit a pull request explaining your changes.

### **Reporting Issues**

If you encounter bugs or have feature requests, please open an issue on our [GitHub Issues Page](https://github.com/Shubhashish-Chakraborty/pyfilemaster/issues).

## **Future Updates**
We are committed to making **PyFileMaster** a comprehensive file-handling utility. More features and functionalities will be continuously added in future updates to enhance its versatility and meet evolving user needs. <br/>
Stay tuned for exciting new capabilities, and feel free to suggest ideas or improvements by opening an issue on our [GitHub repository](https://www.github.com/Shubhashish-Chakraborty/pyfilemaster)!

## **License**

This project is Licensed under the [MIT License](LICENSE) <br/>
Feel free to use, modify, and distribute this project in your own applications while respecting the terms of the license.

# **Connect with the Author**

Created and maintained by [Shubhashish Chakraborty](https://shubhlinks.vercel.app) <br/>
For any queries, reach out via email at shubhashish147@gmail.com. <br/>
PyPi Profile: [beingshubh || Shubhashish Chakraborty](https://pypi.org/user/beingshubh/)

<br/>

[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?logo=Twitter&logoColor=white)](https://twitter.com/__Shubhashish__)
[![Instagram](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://instagram.com/___shubhashish___)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://linkedin.com/in/shubhashish-chakraborty)
[![GitHub](https://img.shields.io/badge/GitHub-%2312100E.svg?logo=github&logoColor=white)](https://github.com/Shubhashish-Chakraborty)

![PyPI](https://img.shields.io/pypi/v/pyfilemaster)  
![GitHub contributors](https://img.shields.io/github/contributors/Shubhashish-Chakraborty/pyfilemaster)  
![GitHub stars](https://img.shields.io/github/stars/Shubhashish-Chakraborty/pyfilemaster)  
![GitHub license](https://img.shields.io/github/license/Shubhashish-Chakraborty/pyfilemaster)  
