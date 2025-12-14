class LanguageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Language Dictionary App")
        self.geometry("400*300")

        self.language_var = tk.StringVar(value="English")
        self.word_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
            language_label = tk.Label(self, text="select language:")
            language_label.pack(pady=10)

            language_menu = ttk.Combobox(self, textvariable=self.language_var, values=list(language_label.keys())
            language_menu.pack(pady=10)

            word_label = tk.Label(self, text="Enter Word:")
            word_label.pack(pady=10)

            word_entry = tk.Entry(self, textvariable=self.word_var)
            word_entry.pack(pady=10)

            search_button = tk.Button(self, text="search", command=self.search_word_))
            search_button.pack(pady=10)


            self.result_label = tk.Label(self, text="")
            self.result_label.pack(pady=10)

    def search_word(self):
                language = self.language_var.get()
                word = self.word_var.get().lower()
                translation = language_dicts.get(language,{}).get(word,"word not found")
                self.result_label.config(text=f"(word.capitalize()) in (language): (translation)")

if __name__ == "__main__":
    app = LanguageApp


