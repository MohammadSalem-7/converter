import tkinter as tk

eng_to_ar = {
    'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف',
    'y': 'غ', 'u': 'ع', 'i': 'ه', 'o': 'خ', 'p': 'ح',
    'a': 'ش', 's': 'س', 'd': 'ي', 'f': 'ب', 'g': 'ل',
    'h': 'ا', 'j': 'ت', 'k': 'ن', 'l': 'م',
    'z': 'ئ', 'x': 'ء', 'c': 'ؤ', 'v': 'ر', 'b': 'لا',
    'n': 'ى', 'm': 'ة',
    'Q': 'َ', 'W': 'ً', 'E': 'ُ', 'R': 'ٌ', 'T': 'لإ',
    'Y': 'إ', 'U': '‘', 'I': '÷', 'O': '×', 'P': '؛',
    'A': 'ِ', 'S': 'ٍ', 'D': ']', 'F': '[', 'G': 'لأ',
    'H': 'أ', 'J': 'ـ', 'K': '،', 'L': '/',
    'Z': '~', 'X': 'ْ', 'C': '}', 'V': '{', 'B': 'لآ',
    'N': 'آ', 'M': '’',
    '`': 'ذ', '[': 'ج', ']': 'د', ';': 'ك', "'": 'ط',
    ',': 'و', '.': 'ز', '/': 'ظ',
    '{': 'ج', '}': 'د'
}

def convert_to_arabic(text):
    text = str(text).strip()
    result = ""
    debug_info = []
    for ch in text:
        unicode_val = ord(ch)
        mapped = eng_to_ar.get(ch, ch)
        debug_info.append(f"Char: '{ch}' (Unicode: {unicode_val}) -> '{mapped}'")
        result += mapped
    print("Input text:", repr(text))
    print("Debug Info:")
    print("\n".join(debug_info))
    print("Output:", repr(result))
    status_label.config(text="\n".join(debug_info[:5]), fg="blue")
    return result

def on_convert():
    wrong_text = input_box.get().strip()
    print("Raw input from Entry widget:", repr(wrong_text))
    converted = convert_to_arabic(wrong_text)
    output_box.delete(0, tk.END)
    output_box.insert(0, converted)

def on_test_bracket():
    test_text = "]"
    input_box.delete(0, tk.END)
    input_box.insert(0, test_text)
    converted = convert_to_arabic(test_text)
    output_box.delete(0, tk.END)
    output_box.insert(0, converted)

def on_test_symbols():
    test_text = "`[];'.,/"
    input_box.delete(0, tk.END)
    input_box.insert(0, test_text)
    converted = convert_to_arabic(test_text)
    output_box.delete(0, tk.END)
    output_box.insert(0, converted)

def on_copy():
    text = output_box.get().strip()
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        root.update()
        status_label.config(text="✔ تم نسخ النص!", fg="green")

def on_clear():
    input_box.delete(0, tk.END)
    output_box.delete(0, tk.END)
    status_label.config(text="")

root = tk.Tk()
root.title("تحويل الكتابة من إنجليزي إلى عربي")
root.geometry("500x400")

tk.Label(root, text="النص المكتوب بالإنجليزي/رموز:", anchor="e").pack(fill="x", padx=10)
input_box = tk.Entry(root, width=50, font=("Tahoma", 12))
input_box.pack(fill="x", padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="تحويل", command=on_convert, width=10, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="اختبار ]", command=on_test_bracket, width=10, bg="#FFC107", fg="black").grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="اختبار رموز", command=on_test_symbols, width=10, bg="#FF5722", fg="white").grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="نسخ", command=on_copy, width=10, bg="#2196F3", fg="white").grid(row=0, column=3, padx=5)
tk.Button(btn_frame, text="مسح", command=on_clear, width=10, bg="#f44336", fg="white").grid(row=0, column=4, padx=5)

tk.Label(root, text="النص بعد التحويل:", anchor="e").pack(fill="x", padx=10)
output_box = tk.Entry(root, width=50, font=("Tahoma", 12))
output_box.pack(fill="x", padx=10)

status_label = tk.Label(root, text="", fg="blue", justify="left", anchor="w", wraplength=480)
status_label.pack(fill="x", padx=10)

root.mainloop()