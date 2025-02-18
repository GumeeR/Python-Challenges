# 🌳 Family Tree

This challenge consists of implementing a **family tree management system** in Python, allowing users to add, remove, and modify family relationships interactively via the terminal 🦝.

## 📌 Features

- 📌 **Add people** with a unique identifier.
- 💍 **Assign partners** to registered individuals.
- 👶 **Add children** to existing parents.
- ❌ **Remove people or relationships** (partners and children).
- 📜 **Visualize the family tree** in the terminal with enhanced formatting using `rich`.

## 🛠️ Requirements

- Python 3.x
- `rich` library for styled terminal output:

    ```bash
    pip install rich
    ```

## 🚀 Usage

1. **Run the program**:

    ```bash
    python main.py
    ```

2. **Select an option** from the menu to manage the family tree:

    ```
    [1] Add Person
    [2] Remove Person
    [3] Modify Partner
    [4] Add Child
    [5] Remove Child
    [6] Print Family Tree
    [7] Exit
    ```

3. **Example workflow**:

    - Add a person with ID 1 named "Carlos."
    - Add a person with ID 2 named "Ana" and assign her as Carlos' partner.
    - Add a person with ID 3 named "Luis" and assign him as Carlos' child.

4. **Expected output when printing the tree**:

    ```
    --- Family Tree ---
    Carlos (ID: 1)
      Partner: Ana
      Child: Luis (ID: 3)
    Ana (ID: 2)
      Partner: Carlos
    Luis (ID: 3)
      Partner: None
    ```
