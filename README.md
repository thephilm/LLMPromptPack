# **LLMPromptPack**  

LLMPromptPack takes a folder and converts it into a structured text file.  
This is useful when working with an LLM (via UI or API) and you want to provide a **full site structure** without uploading individual files.  

The generated text file can later be **extracted back into files** using the **LLMPromptUnpack** script.  

---

## **Installation Requirements**  
- Requires **Python**  
- Requires **Tkinter** (included in most Python installations)  

---

## **Usage**  

Run from the command line:  
python llm_prompt_pack.py

1. **Tkinter** will launch and prompt you to choose a folder.  
2. The script will scan all files under the selected folder.  
3. A directory tree will be displayed, showing all included files.  
4. Each file will have its own section in the text document, marked with **beginning and end notation**.  

### **File Filtering**  
- You can **include or omit** files based on extensions.  
- By default, the following file types are included:  
target_extensions = ['.js', '.py', '.txt', '.xml', '.html', '.css']
- To customize, edit `target_extensions` in the script.

---

## **Output**  
- The output file will be named:  
project_contents_YYYY-MM-DD_HH-MM-SS.txt
- This format ensures that multiple exports can be easily organized.  
- **LLMPromptUnpack** can later reconstruct files from this text document into the original folder structure.

---

## **Example Use Case**  
1. Select a **website project folder**.  
2. **LLMPromptPack** converts the entire structure into a single `.txt` file.  
3. Use the text file as **input for an LLM** (via UI or API).  
4. Later, **LLMPromptUnpack** reconstructs the project from the text.

---

### **Future Improvements**
- Add support for **additional file types**.
- Allow **custom include/exclude rules**.
- Implement **CLI flags** for automation.

---

### **License**
MIT License – Free to use and modify.

---

**Created by Philip Mastroianni**  
