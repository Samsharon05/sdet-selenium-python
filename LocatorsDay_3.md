# Day 3 - Locators (CSS & XPath)

---

## Login Page

### Username
- **CSS:** `#userName`
- **XPath:** `//input[@id="userName"]`

---

### Password
- **CSS:** `input[placeholder="Password"]`
- **XPath:** `//input[@placeholder="Password"]`

---

### Login Button
- **CSS:** `button[class="btn btn-primary"]:nth-of-type(1)`
- **XPath:** `(//button[@class="btn btn-primary"])[1]`

---

### New User Button
- **CSS:** `div.button.col-auto:nth-of-type(2) button`
- **XPath:** `(//button[@type="button"])[3]`

---

## Book Selection

### Select Item
- **CSS:** `a[href="/books?search=9781449325862"]`
- **XPath:** `//a[@href="/books?search=9781449325862"]`

---

### Add to Your Collection
- **CSS:** `div:nth-of-type(2) button[id="addNewRecordButton"]`
- **XPath:** `(//button[@id="addNewRecordButton"])[2]`

---

## Practice Form

### First Name
- **CSS:** `input[placeholder="First Name"]`
- **XPath:** `//input[@placeholder="First Name"]`

---

### Last Name
- **CSS:** `input[placeholder="Last Name"]`
- **XPath:** `//input[@placeholder="Last Name"]`

---

### Email
- **CSS:** `input[class="mr-sm-2 form-control"]`
- **XPath:** `//input[@class="mr-sm-2 form-control"]`

---

### Gender (Male Radio Button)
- **CSS:** `input[name="gender"][value="Male"]`
- **XPath:** `(//input[@type="radio"])[1]`

---

### Mobile Number
- **CSS:** `input[placeholder="Mobile Number"]`
- **XPath:** `//input[@placeholder="Mobile Number"]`

---

### Hobbies
- **CSS:** `#hobbies-checkbox-1`
- **XPath:** `//input[@id="hobbies-checkbox-1"]`

---