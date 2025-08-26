import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import json
import webbrowser
from datetime import datetime
import threading

class ModernClashRoyaleUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Clash Royale Level Calculator")
        self.root.geometry("1300x1000")
        self.root.configure(bg='#2c3e50')
        
        # Modern color scheme
        self.colors = {
            'bg_dark': '#2c3e50',
            'bg_medium': '#34495e',
            'bg_light': '#ecf0f1',
            'accent': '#3498db',
            'success': '#27ae60',
            'error': '#e74c3c',
            'warning': '#f39c12',
            'text_light': '#ecf0f1',
            'text_dark': '#2c3e50'
        }
        
        # Configure styles
        self.setup_styles()
        
        # Variables
        self.player_tag = tk.StringVar()
        self.auth_token = tk.StringVar()
        self.is_validated = False
        self.debug_info = {}
        
        # Create main container
        self.main_frame = tk.Frame(root, bg=self.colors['bg_dark'])
        self.main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Show validation screen initially
        self.show_validation_screen()
    
    def setup_styles(self):
        """Configure modern styles for widgets"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('Modern.TFrame', background=self.colors['bg_dark'])
        style.configure('Card.TFrame', background=self.colors['bg_medium'], relief='flat')
        style.configure('Modern.TLabel', background=self.colors['bg_medium'], foreground=self.colors['text_light'], font=('Segoe UI', 10))
        style.configure('Title.TLabel', background=self.colors['bg_dark'], foreground=self.colors['text_light'], font=('Segoe UI', 16, 'bold'))
        style.configure('Subtitle.TLabel', background=self.colors['bg_dark'], foreground=self.colors['text_light'], font=('Segoe UI', 12))
        style.configure('Modern.TButton', background=self.colors['accent'], foreground=self.colors['text_light'], font=('Segoe UI', 10, 'bold'))
        style.configure('Success.TButton', background=self.colors['success'], foreground=self.colors['text_light'], font=('Segoe UI', 10, 'bold'))
        style.configure('Error.TButton', background=self.colors['error'], foreground=self.colors['text_light'], font=('Segoe UI', 10, 'bold'))
    
    def create_modern_entry(self, parent, placeholder, show=None):
        """Create a modern-looking entry widget"""
        frame = tk.Frame(parent, bg=self.colors['bg_medium'], relief='flat', bd=0)
        
        entry = tk.Entry(frame, 
                        font=('Segoe UI', 10),
                        bg=self.colors['bg_light'],
                        fg=self.colors['text_dark'],
                        relief='flat',
                        bd=10,
                        show=show)
        
        entry.insert(0, placeholder)
        entry.bind('<FocusIn>', lambda e: self.on_entry_focus_in(entry, placeholder))
        entry.bind('<FocusOut>', lambda e: self.on_entry_focus_out(entry, placeholder))
        
        entry.pack(fill='x', padx=10, pady=5)
        return frame, entry
    
    def on_entry_focus_in(self, entry, placeholder):
        """Handle entry focus in"""
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg=self.colors['text_dark'])
    
    def on_entry_focus_out(self, entry, placeholder):
        """Handle entry focus out"""
        if entry.get() == '':
            entry.insert(0, placeholder)
            entry.config(fg='gray')
    
    def create_modern_button(self, parent, text, command, style='Modern'):
        """Create a modern-looking button"""
        button = tk.Button(parent,
                          text=text,
                          command=command,
                          font=('Segoe UI', 10, 'bold'),
                          bg=self.colors['accent'],
                          fg=self.colors['text_light'],
                          relief='flat',
                          bd=0,
                          padx=20,
                          pady=10,
                          cursor='hand2')
        
        button.bind('<Enter>', lambda e: button.config(bg='#2980b9'))
        button.bind('<Leave>', lambda e: button.config(bg=self.colors['accent']))
        
        return button
    
    def show_validation_screen(self):
        """Show the validation screen"""
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Title
        title_label = tk.Label(self.main_frame, 
                              text="Clash Royale Calculator",
                              font=('Segoe UI', 24, 'bold'),
                              bg=self.colors['bg_dark'],
                              fg=self.colors['text_light'])
        title_label.pack(pady=(0, 10))
        
        subtitle_label = tk.Label(self.main_frame,
                                 text="Enter your credentials to access the tool",
                                 font=('Segoe UI', 12),
                                 bg=self.colors['bg_dark'],
                                 fg=self.colors['text_light'])
        subtitle_label.pack(pady=(0, 30))
        
        # Card container
        card_frame = tk.Frame(self.main_frame, bg=self.colors['bg_medium'], relief='flat', bd=0)
        card_frame.pack(fill='x', padx=50)
        
        # Player Tag
        tag_label = tk.Label(card_frame,
                            text="Enter Player Tag:",
                            font=('Segoe UI', 11, 'bold'),
                            bg=self.colors['bg_medium'],
                            fg=self.colors['text_light'],
                            anchor='w')
        tag_label.pack(fill='x', padx=20, pady=(20, 5))
        
        tag_entry_frame, self.tag_entry = self.create_modern_entry(card_frame, "e.g., UU8R2V8J")
        tag_entry_frame.pack(fill='x', padx=20, pady=(0, 10))
        
        tag_hint = tk.Label(card_frame,
                           text="Must be 7, 8, or 9 characters (letters and numbers)",
                           font=('Segoe UI', 9),
                           bg=self.colors['bg_medium'],
                           fg='#bdc3c7',
                           anchor='w')
        tag_hint.pack(fill='x', padx=20, pady=(0, 15))
        
        # Auth Token
        token_label = tk.Label(card_frame,
                              text="Enter API Token:",
                              font=('Segoe UI', 11, 'bold'),
                              bg=self.colors['bg_medium'],
                              fg=self.colors['text_light'],
                              anchor='w')
        token_label.pack(fill='x', padx=20, pady=(0, 5))
        
        token_entry_frame, self.token_entry = self.create_modern_entry(card_frame, "Enter your Clash Royale API token", show="*")
        token_entry_frame.pack(fill='x', padx=20, pady=(0, 10))
        
        token_hint = tk.Label(card_frame,
                             text="Get your token from developer.clashroyale.com",
                             font=('Segoe UI', 9),
                             bg=self.colors['bg_medium'],
                             fg='#bdc3c7',
                             anchor='w')
        token_hint.pack(fill='x', padx=20, pady=(0, 20))
        
        # Validate Button
        self.validate_button = self.create_modern_button(card_frame, "Validate Credentials", self.validate_credentials)
        self.validate_button.pack(pady=20)
        
        # Debug info area
        self.debug_text = scrolledtext.ScrolledText(card_frame,
                                                   height=8,
                                                   font=('Consolas', 9),
                                                   bg='#1a1a1a',
                                                   fg='#00ff00',
                                                   relief='flat',
                                                   bd=0)
        self.debug_text.pack(fill='x', padx=20, pady=(0, 20))
        self.debug_text.insert(tk.END, "Debug information will appear here...\n")
        self.debug_text.config(state='disabled')
    
    def validate_credentials(self):
        """Validate the entered credentials"""
        player_tag = self.tag_entry.get().strip().upper()
        # Allow users to paste tags with leading '#'
        if player_tag.startswith('#'):
            player_tag = player_tag[1:]
        auth_token = self.token_entry.get().strip()
        # Remove any internal whitespace/newlines from token to avoid invalid header
        auth_token = ''.join(auth_token.split())
        
        # Clear debug
        self.debug_text.config(state='normal')
        self.debug_text.delete(1.0, tk.END)
        self.debug_text.config(state='disabled')
        
        # Validate format
        if not player_tag or player_tag == "e.g., UU8R2V8J":
            self.show_error("Please enter a valid player tag")
            return
        
        if not auth_token or auth_token == "Enter your Clash Royale API token":
            self.show_error("Please enter a valid API token")
            return
        
        # Validate player tag format: must be alphanumeric and length 7, 8, or 9
        if (not player_tag.isalnum()) or (len(player_tag) not in (7, 8, 9)):
            self.show_error("Player tag must be 7, 8, or 9 characters (letters and numbers)")
            return
        
        # Disable button and show loading
        self.validate_button.config(text="Validating...", state='disabled')
        self.root.update()
        
        # Run validation in thread to avoid blocking UI
        thread = threading.Thread(target=self.perform_validation, args=(player_tag, auth_token))
        thread.daemon = True
        thread.start()
    
    def perform_validation(self, player_tag, auth_token):
        """Perform the actual API validation"""
        try:
            # Test API call
            url = f"https://api.clashroyale.com/v1/players/%23{player_tag}"
            headers = {
                'Accept': 'application/json',
                'Authorization': f'Bearer {auth_token}'
            }
            
            response = requests.get(url, headers=headers, timeout=10)
            
            debug_data = {
                'statusCode': response.status_code,
                'statusText': response.reason,
                'playerTag': player_tag,
                'authToken': auth_token,
                'tokenLength': len(auth_token),
                'timestamp': datetime.now().isoformat()
            }
            
            if response.ok:
                player_data = response.json()
                debug_data.update({
                    'playerName': player_data.get('name'),
                    'playerLevel': player_data.get('expLevel'),
                    'trophies': player_data.get('trophies'),
                    'success': True
                })
                
                # Update UI on main thread
                self.root.after(0, lambda: self.show_success(debug_data))
            else:
                # Provide clearer messaging depending on failure type
                if response.status_code == 404:
                    msg = "Player tag appears to be incorrect or not found. Length is valid but the tag does not match any player."
                elif response.status_code in (401, 403):
                    msg = "API token is invalid or not authorized for your IP. Please check your token."
                else:
                    msg = f"Validation failed: {response.status_code} - {response.reason}"
                debug_data['error'] = msg
                self.root.after(0, lambda: self.show_error(msg, debug_data))
                
        except requests.exceptions.RequestException as e:
            error_msg = str(e)
            debug_data = {
                'error': error_msg,
                'playerTag': player_tag,
                'authToken': auth_token,
                'tokenLength': len(auth_token),
                'timestamp': datetime.now().isoformat()
            }
            self.root.after(0, lambda: self.show_error(f"Network error: {error_msg}", debug_data))
    
    def show_error(self, message, debug_data=None):
        """Show error message"""
        self.validate_button.config(text="Validate Credentials", state='normal')
        
        if debug_data:
            self.update_debug_info(debug_data)
        
        messagebox.showerror("Validation Error", message)
    
    def show_success(self, debug_data):
        """Show success screen and automatically calculate"""
        self.is_validated = True
        self.debug_info = debug_data
        self.show_success_screen()
        
        # Automatically start calculation
        self.calculate_max_level()
    
    def show_success_screen(self):
        """Show the success screen with calculator"""
        # Clear main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # App title
        title_label = tk.Label(self.main_frame,
                              text="Welcome to Louis' Clash Level Calculator",
                              font=('Segoe UI', 24, 'bold'),
                              bg=self.colors['bg_dark'],
                              fg=self.colors['text_light'])
        title_label.pack(pady=(0, 6))
        # GitHub link
        link = tk.Label(self.main_frame,
                        text="GitHub: louiscross/ClashRoyale-API-Level-Calculator",
                        font=('Segoe UI', 10, 'underline'),
                        bg=self.colors['bg_dark'],
                        fg=self.colors['accent'],
                        cursor='hand2')
        link.pack(pady=(0, 12))
        link.bind("<Button-1>", lambda e: webbrowser.open_new_tab("https://github.com/louiscross/ClashRoyale-API-Level-Calculator"))
        
        # Card container
        card_frame = tk.Frame(self.main_frame, bg=self.colors['bg_medium'], relief='flat', bd=0)
        card_frame.pack(fill='x', padx=50)
        
        # Welcome message
        welcome_label = tk.Label(card_frame,
                                text="Welcome to Clash Royale Calculator",
                                font=('Segoe UI', 16, 'bold'),
                                bg=self.colors['bg_medium'],
                                fg=self.colors['text_light'])
        welcome_label.pack(pady=(20, 10))
        
        desc_label = tk.Label(card_frame,
                             text="Calculating your maximum achievable level...",
                             font=('Segoe UI', 12),
                             bg=self.colors['bg_medium'],
                             fg=self.colors['text_light'])
        desc_label.pack(pady=(0, 20))
        
        # Loading indicator
        self.loading_label = tk.Label(card_frame,
                                     text="⏳ Loading...",
                                     font=('Segoe UI', 14, 'bold'),
                                     bg=self.colors['bg_medium'],
                                     fg=self.colors['accent'])
        self.loading_label.pack(pady=20)
        
        # Controls row: switch player tag + gold input + recalc
        controls_frame = tk.Frame(card_frame, bg=self.colors['bg_medium'], relief='flat', bd=0)
        controls_frame.pack(fill='x', padx=20, pady=(0, 10))

        # Switch player tag
        tag_switch_label = tk.Label(controls_frame,
                                    text="Player Tag:",
                                    font=('Segoe UI', 10, 'bold'),
                              bg=self.colors['bg_medium'],
                                    fg=self.colors['text_light'])
        tag_switch_label.grid(row=0, column=0, sticky='w')

        self.player_switch_entry = tk.Entry(controls_frame,
                                            font=('Segoe UI', 10),
                                            bg=self.colors['bg_light'],
                                            fg=self.colors['text_dark'],
                                              relief='flat',
                                            bd=8)
        # Pre-fill with current validated tag
        self.player_switch_entry.insert(0, self.debug_info.get('playerTag', ''))
        self.player_switch_entry.grid(row=0, column=1, padx=10, pady=5, sticky='we')

        switch_button = self.create_modern_button(controls_frame, "Load Player", self.switch_player)
        switch_button.grid(row=0, column=2, padx=(10, 0))

        # Gold budget input
        gold_label = tk.Label(controls_frame,
                              text="Gold:",
                              font=('Segoe UI', 10, 'bold'),
                              bg=self.colors['bg_medium'],
                              fg=self.colors['text_light'])
        gold_label.grid(row=0, column=3, sticky='w', padx=(20, 0))

        self.gold_entry = tk.Entry(controls_frame,
                                   font=('Segoe UI', 10),
                                   bg=self.colors['bg_light'],
                                   fg=self.colors['text_dark'],
                                   relief='flat',
                                   bd=8)
        self.gold_entry.insert(0, "Enter available gold (e.g., 250,000)")
        self.gold_entry.bind('<FocusIn>', lambda e: self.on_entry_focus_in(self.gold_entry, "Enter available gold (e.g., 250,000)"))
        self.gold_entry.bind('<FocusOut>', lambda e: self.on_entry_focus_out(self.gold_entry, "Enter available gold (e.g., 250,000)"))
        self.gold_entry.grid(row=0, column=4, padx=10, pady=5, sticky='we')

        recalc_button = self.create_modern_button(controls_frame, "Recalculate", self.calculate_max_level)
        recalc_button.grid(row=0, column=5, padx=(10, 0))

        controls_frame.grid_columnconfigure(1, weight=1)
        controls_frame.grid_columnconfigure(4, weight=1)

        # Top-left options: verbose + include magic items (larger, clearer)
        options_frame = tk.Frame(card_frame, bg=self.colors['bg_medium'], relief='flat', bd=0)
        options_frame.pack(fill='x', padx=20, pady=(0, 6))

        self.verbose_var = tk.BooleanVar(value=False)
        verbose_check = tk.Checkbutton(options_frame,
                                       text="Verbose console logs",
                                       variable=self.verbose_var,
                                       onvalue=True,
                                       offvalue=False,
                                       bg=self.colors['bg_medium'],
                                       fg=self.colors['text_light'],
                                       activebackground=self.colors['bg_medium'],
                                       activeforeground=self.colors['text_light'],
                                       selectcolor=self.colors['bg_medium'])
        verbose_check.grid(row=0, column=0, sticky='w')

        self.magic_toggle_var = tk.BooleanVar(value=False)
        magic_toggle = tk.Checkbutton(options_frame,
                                      text="Include Magic Items",
                                      variable=self.magic_toggle_var,
                                      onvalue=True,
                                      offvalue=False,
                                      bg=self.colors['bg_medium'],
                                      fg=self.colors['text_light'],
                                      activebackground=self.colors['bg_medium'],
                                      activeforeground=self.colors['text_light'],
                                      selectcolor=self.colors['bg_medium'],
                                      font=('Segoe UI', 12, 'bold'),
                                      padx=10,
                                      command=self.toggle_magic_panel)
        magic_toggle.grid(row=0, column=1, sticky='w', padx=(20, 0))
        options_frame.grid_columnconfigure(2, weight=1)

        self.magic_panel = tk.Frame(card_frame, bg=self.colors['bg_medium'], relief='flat', bd=0)
        # Two-column layout for tidy alignment
        columns = self.magic_panel
        columns.grid_columnconfigure(0, weight=1)
        columns.grid_columnconfigure(1, weight=1)

        wild_frame = tk.Frame(columns, bg=self.colors['bg_medium'])
        book_frame = tk.Frame(columns, bg=self.colors['bg_medium'])
        coin_frame = tk.Frame(columns, bg=self.colors['bg_medium'])
        wild_frame.grid(row=0, column=0, sticky='nwe', padx=10)
        book_frame.grid(row=0, column=1, sticky='nwe', padx=10)
        coin_frame.grid(row=1, column=0, columnspan=2, sticky='we', padx=10, pady=(6, 0))

        def add_labeled_entry_grid(parent, row_index, label_text):
            lbl = tk.Label(parent, text=label_text, font=('Segoe UI', 10), bg=self.colors['bg_medium'], fg=self.colors['text_light'])
            lbl.grid(row=row_index, column=0, sticky='w', pady=2)
            ent = tk.Entry(parent, font=('Segoe UI', 10), bg=self.colors['bg_light'], fg=self.colors['text_dark'], relief='flat', bd=4, width=10)
            ent.insert(0, '0')
            ent.grid(row=row_index, column=1, sticky='we', pady=2, padx=(10, 0))
            parent.grid_columnconfigure(1, weight=1)
            return ent

        # Wildcards
        tk.Label(wild_frame, text="Wild Cards (by rarity)", font=('Segoe UI', 11, 'bold'), bg=self.colors['bg_medium'], fg=self.colors['text_light']).grid(row=0, column=0, columnspan=2, sticky='w', pady=(6, 4))
        self.common_wc_entry = add_labeled_entry_grid(wild_frame, 1, "Common Wild Cards:")
        self.rare_wc_entry = add_labeled_entry_grid(wild_frame, 2, "Rare Wild Cards:")
        self.epic_wc_entry = add_labeled_entry_grid(wild_frame, 3, "Epic Wild Cards:")
        self.legendary_wc_entry = add_labeled_entry_grid(wild_frame, 4, "Legendary Wild Cards:")
        self.champion_wc_entry = add_labeled_entry_grid(wild_frame, 5, "Champion Wild Cards:")
        self.elite_wc_entry = add_labeled_entry_grid(wild_frame, 6, "Elite Wild Cards:")

        # Books
        tk.Label(book_frame, text="Books (by rarity)", font=('Segoe UI', 11, 'bold'), bg=self.colors['bg_medium'], fg=self.colors['text_light']).grid(row=0, column=0, columnspan=2, sticky='w', pady=(6, 4))
        self.common_book_entry = add_labeled_entry_grid(book_frame, 1, "Book of Commons:")
        self.rare_book_entry = add_labeled_entry_grid(book_frame, 2, "Book of Rares:")
        self.epic_book_entry = add_labeled_entry_grid(book_frame, 3, "Book of Epics:")
        self.legendary_book_entry = add_labeled_entry_grid(book_frame, 4, "Book of Legendaries:")
        self.champion_book_entry = add_labeled_entry_grid(book_frame, 5, "Book of Champions:")
        # Only use books for L14 toggle (applies to all rarities)
        self.only_books_level14_var = tk.BooleanVar(value=True)
        only_books_l14 = tk.Checkbutton(book_frame,
                                        text="Only use books for level 14",
                                        variable=self.only_books_level14_var,
                                        onvalue=True,
                                        offvalue=False,
                                        bg=self.colors['bg_medium'],
                                        fg=self.colors['text_light'],
                                        activebackground=self.colors['bg_medium'],
                                        activeforeground=self.colors['text_light'],
                                        selectcolor=self.colors['bg_medium'])
        only_books_l14.grid(row=6, column=0, columnspan=2, sticky='w', pady=(6, 0))

        # Magic coin
        tk.Label(coin_frame, text="Magic Coins", font=('Segoe UI', 11, 'bold'), bg=self.colors['bg_medium'], fg=self.colors['text_light']).grid(row=0, column=0, sticky='w', pady=(6, 4))
        self.magic_coin_entry = tk.Entry(coin_frame, font=('Segoe UI', 10), bg=self.colors['bg_light'], fg=self.colors['text_dark'], relief='flat', bd=4, width=10)
        self.magic_coin_entry.insert(0, '0')
        self.magic_coin_entry.grid(row=0, column=1, sticky='w', padx=(10, 10))
        # Only use coins for L13->L14 toggle
        self.only_coin_level14_var = tk.BooleanVar(value=True)
        only_l14 = tk.Checkbutton(coin_frame,
                                  text="Only use coins for level 14",
                                  variable=self.only_coin_level14_var,
                                  onvalue=True,
                                  offvalue=False,
                                  bg=self.colors['bg_medium'],
                                  fg=self.colors['text_light'],
                                  activebackground=self.colors['bg_medium'],
                                  activeforeground=self.colors['text_light'],
                                  selectcolor=self.colors['bg_medium'])
        only_l14.grid(row=0, column=2, sticky='w')

        # Hide panel initially
        self.magic_panel.pack_forget()

        # Results area (scrollable) - placed after controls so controls are visible at top
        self.results_container = tk.Frame(card_frame, bg=self.colors['bg_medium'], relief='flat', bd=0)
        self.results_container.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        container_height = 420
        self.results_canvas = tk.Canvas(self.results_container,
                                        bg=self.colors['bg_medium'],
                                        highlightthickness=0,
                                        height=container_height)
        self.results_scrollbar = tk.Scrollbar(self.results_container, orient='vertical', command=self.results_canvas.yview)
        self.results_inner = tk.Frame(self.results_canvas, bg=self.colors['bg_medium'], relief='flat', bd=0)
        self.results_inner.bind('<Configure>', lambda e: self.results_canvas.configure(scrollregion=self.results_canvas.bbox('all')))
        self.results_canvas.create_window((0, 0), window=self.results_inner, anchor='nw')
        self.results_canvas.configure(yscrollcommand=self.results_scrollbar.set)
        self.results_canvas.pack(side='left', fill='both', expand=True)
        self.results_scrollbar.pack(side='right', fill='y')
        # Mouse wheel scrolling
        def _on_mousewheel(event):
            # Windows delta is multiples of 120
            delta = int(-1*(event.delta/120))
            self.results_canvas.yview_scroll(delta, 'units')
        self.results_canvas.bind_all('<MouseWheel>', _on_mousewheel)
        
        # Reset button
        reset_button = self.create_modern_button(card_frame, "Reset Validation", self.reset_validation)
        reset_button.pack(pady=20)

    def toggle_magic_panel(self):
        """Show or hide the magic items input panel based on the toggle."""
        try:
            enabled = bool(self.magic_toggle_var.get())
        except Exception:
            enabled = False
        if enabled:
            # Show panel
            if hasattr(self, 'magic_panel') and self.magic_panel is not None:
                self.magic_panel.pack(fill='x', padx=0, pady=(5, 10))
                try:
                    # Expand window size a bit more to comfortably fit panel
                    self.root.geometry("1300x1150")
                except Exception:
                    pass
        else:
            # Hide panel
            if hasattr(self, 'magic_panel') and self.magic_panel is not None:
                self.magic_panel.pack_forget()
                try:
                    # Restore to default size
                    self.root.geometry("1000x1000")
                except Exception:
                    pass
        

    def update_debug_info(self, debug_data):
        """Update debug information display"""
        self.debug_text.config(state='normal')
        self.debug_text.delete(1.0, tk.END)
        self.debug_text.insert(tk.END, json.dumps(debug_data, indent=2))
        self.debug_text.config(state='disabled')
    
    def calculate_max_level(self):
        """Calculate maximum level using existing Python logic"""
        # Get credentials from debug info (stored during validation)
        # Allow switching player tag from UI
        player_tag = ''
        if hasattr(self, 'player_switch_entry') and self.player_switch_entry is not None:
            player_tag = self.player_switch_entry.get().strip().upper()
            if player_tag.startswith('#'):
                player_tag = player_tag[1:]
        if not player_tag:
            player_tag = self.debug_info.get('playerTag', '')
        auth_token = self.debug_info.get('authToken', '')
        
        # Parse available gold from UI input
        available_gold = 0
        if hasattr(self, 'gold_entry') and self.gold_entry is not None:
            raw = self.gold_entry.get().strip()
            if raw and raw != "Enter available gold (e.g., 250,000)":
                digits = ''.join(ch for ch in raw if ch.isdigit())
                available_gold = int(digits) if digits else 0
        verbose = bool(getattr(self, 'verbose_var', tk.BooleanVar(value=False)).get())
        # Parse magic items if enabled
        def parse_int(entry):
            try:
                s = entry.get().strip()
                digits = ''.join(ch for ch in s if ch.isdigit())
                return int(digits) if digits else 0
            except Exception:
                return 0
        magic_items = None
        if getattr(self, 'magic_toggle_var', tk.BooleanVar(value=False)).get():
            magic_items = {
                'wildcards': {
                    'common': parse_int(self.common_wc_entry),
                    'rare': parse_int(self.rare_wc_entry),
                    'epic': parse_int(self.epic_wc_entry),
                    'legendary': parse_int(self.legendary_wc_entry),
                    'champion': parse_int(self.champion_wc_entry),
                    'elite': parse_int(self.elite_wc_entry),
                },
                'books': {
                    'common': parse_int(self.common_book_entry),
                    'rare': parse_int(self.rare_book_entry),
                    'epic': parse_int(self.epic_book_entry),
                    'legendary': parse_int(self.legendary_book_entry),
                    'champion': parse_int(self.champion_book_entry),
                    'only_books_level14': bool(getattr(self, 'only_books_level14_var', tk.BooleanVar(value=False)).get())
                },
                'magic_coins': parse_int(self.magic_coin_entry),
                'only_coins_level14': bool(getattr(self, 'only_coin_level14_var', tk.BooleanVar(value=True)).get())
            }
        
        # Run calculation in thread to avoid blocking UI
        thread = threading.Thread(target=self.perform_calculation, args=(player_tag, auth_token, available_gold, verbose, magic_items))
        thread.daemon = True
        thread.start()
    
    def switch_player(self):
        """Update the current player tag and trigger recalculation"""
        # Validate new tag format
        new_tag = self.player_switch_entry.get().strip().upper() if hasattr(self, 'player_switch_entry') else ''
        if new_tag.startswith('#'):
            new_tag = new_tag[1:]
        if (not new_tag) or (not new_tag.isalnum()) or (len(new_tag) not in (7, 8, 9)):
            self.show_error("Player tag must be 7, 8, or 9 characters (letters and numbers)")
            return
        # Update debug_info store and recalc
        self.debug_info['playerTag'] = new_tag
        self.calculate_max_level()
    
    def perform_calculation(self, player_tag, auth_token, available_gold, verbose, magic_items):
        """Perform the level calculation using existing logic"""
        try:
            # Import your existing classes
            from API import Main
            import io
            import sys
            
            # Create main instance with validated credentials
            main_instance = Main(player_tag, auth_token)
            
            # Optionally capture the output from the run method when not verbose
            if verbose:
                captured_output = None
                old_stdout = None
            else:
                captured_output = io.StringIO()
                old_stdout = sys.stdout
                sys.stdout = captured_output
            
            try:
                # Call the run method but intercept the input
                # We'll need to modify the run method to accept a parameter
                # For now, let's create a modified version that calculates max level
                self.calculate_max_level_with_existing_logic(main_instance, player_tag, available_gold, verbose, magic_items)
                
                # Get the captured output
                output = captured_output.getvalue() if captured_output is not None else ""
                
                # Parse the results from the output
                results = self.parse_results_from_output(output, player_tag)
                
                # Update UI on main thread
                self.root.after(0, lambda: self.show_calculation_results(results))
                
            finally:
                # Restore stdout
                if old_stdout is not None:
                    sys.stdout = old_stdout
                if captured_output is not None:
                    captured_output.close()
                
        except Exception as e:
            error_msg = f"Calculation error: {str(e)}"
            self.root.after(0, lambda: self.show_calculation_error(error_msg))
    
    def calculate_max_level_with_existing_logic(self, main_instance, player_tag, available_gold=0, verbose=False, magic_items=None):
        """Use the existing API logic to calculate maximum level"""
        try:
            # Get player data using the existing method
            response = requests.get(f"https://api.clashroyale.com/v1/players/%23{player_tag}", headers=main_instance.headers)
            
            if response.status_code == 200:
                player_data = response.json()
                
                # Use existing methods from API.py
                account = main_instance.getAccount(player_data)
                # Override gold with user-provided available_gold if given
                if isinstance(available_gold, int) and available_gold >= 0:
                    account.gold = available_gold
                cards = player_data['cards']
                card_data = main_instance.getCards(cards, [])

                newcardlist = []
                
                # Load tables using existing methods
                expTable = main_instance.exp_table([])
                upgradeTable = main_instance.upgrade_table([])
                upgradeTableExp = main_instance.upgrade_table_exp([])
                cardRequiredTable = main_instance.card_required_table([])
                
                # Sort cards by level (lowest first) - same as original
                card = sorted(card_data, key=lambda x: x.level, reverse=False)
                
                # Track costs and upgrades
                total_gold_cost = 0
                total_exp_gained = 0
                upgrades_performed = 0
                per_level_cumulative_gold = []

                def log(msg):
                    if verbose:
                        print(msg)

                # Helpers for magic items
                def rarity_from_max_level(max_level):
                    if max_level == 14:
                        return 'common'
                    if max_level == 12:
                        return 'rare'
                    if max_level == 9:
                        return 'epic'
                    if max_level == 6:
                        return 'legendary'
                    if max_level == 4:
                        return 'champion'
                    return 'common'

                def try_cover_with_magic(required_cards, current_count, rarity):
                    """Try to cover deficit with book and wildcards. Returns (can_upgrade, new_count)."""
                    if magic_items is None:
                        return (current_count >= required_cards, current_count)
                    
                    deficit = max(0, required_cards - current_count)
                    if deficit == 0:
                        return (True, current_count)
                    
                    log(f"  Magic items check for {rarity} rarity: deficit={deficit}, current={current_count}, required={required_cards}")
                    
                    # Use book first if allowed and deficit > 0
                    if deficit > 0 and magic_items['books'].get(rarity, 0) > 0:
                        allowed = True
                        if magic_items['books'].get('only_books_level14', False):
                            # Books only allowed when upgrading to level 14
                            target_level = card[0].level + 1
                            allowed = (target_level == 14)
                            log(f"  Book usage check: target_level={target_level}, allowed={allowed}")
                        if allowed:
                            magic_items['books'][rarity] -= 1
                            log(f"  Using Book of {rarity.title()} to cover {deficit} missing cards")
                            current_count = required_cards
                            deficit = 0
                            return (True, current_count)
                    
                    # Use rarity wildcards next
                    if deficit > 0 and magic_items['wildcards'].get(rarity, 0) > 0:
                        use = min(deficit, magic_items['wildcards'][rarity])
                        magic_items['wildcards'][rarity] -= use
                        current_count += use
                        deficit -= use
                        log(f"  Using {use} {rarity.title()} Wild Cards (remaining {magic_items['wildcards'][rarity]})")
                    
                    # Use elite wildcards last, ONLY for L14 -> L15 upgrades
                    target_level = card[0].level + 1
                    if deficit > 0 and target_level == 15 and magic_items['wildcards'].get('elite', 0) > 0:
                        use = min(deficit, magic_items['wildcards']['elite'])
                        magic_items['wildcards']['elite'] -= use
                        current_count += use
                        deficit -= use
                        log(f"  Using {use} Elite Wild Cards (remaining {magic_items['wildcards']['elite']}) for L14->L15")
                    
                    final_can_upgrade = current_count >= required_cards
                    log(f"  Final result: can_upgrade={final_can_upgrade}, final_count={current_count}")
                    return (final_can_upgrade, current_count)
                
                # Run the upgrade loop until no more cards can be upgraded
                while card:
                    if not card:
                        break
                        
                    # Determine rarity index (same logic as original)
                    itemRarityIndex = 0
                    if card[0].maxLevel == 14:
                        itemRarityIndex = 1  # Common
                    elif card[0].maxLevel == 12:
                        itemRarityIndex = 2  # Rare
                    elif card[0].maxLevel == 9:
                        itemRarityIndex = 3  # Epic
                    elif card[0].maxLevel == 6:
                        itemRarityIndex = 4  # Legendary
                    elif card[0].maxLevel == 4:
                        itemRarityIndex = 5  # Champion
                    
                    # Check if card is max level (updated for level 15)
                    if card[0].level == 15:
                        newcardlist.append(card[0])
                        card_data.remove(card[0])
                        card = sorted(card_data, key=lambda x: x.level, reverse=False)
                        continue
                    
                    # Check if enough cards to upgrade (handle possible non-numeric like '50,000 Elite Wild Cards')
                    def safe_to_int(value):
                        s = str(value)
                        if s.upper() == 'N/A':
                            return 0
                        digits = ''.join(ch for ch in s if ch.isdigit())
                        return int(digits) if digits else 0

                    # Use current level index for requirement to next level (e.g., L8->L9 uses row 9)
                    next_level_index = card[0].level
                    if next_level_index >= len(cardRequiredTable):
                        log(f"No further level data for {card[0].name}. Skipping.")
                        newcardlist.append(card[0])
                        card_data.remove(card[0])
                        card = sorted(card_data, key=lambda x: x.level, reverse=False)
                        continue
                    required_cards = safe_to_int(cardRequiredTable[next_level_index][itemRarityIndex])
                    rarity = rarity_from_max_level(card[0].maxLevel)
                    log(f"  Card {card[0].name}: maxLevel={card[0].maxLevel}, determined rarity={rarity}")
                    # Try to cover missing cards with magic items
                    can_upgrade, adjusted_count = try_cover_with_magic(required_cards, int(card[0].count), rarity)
                    card[0].count = adjusted_count
                    log(f"Considering {card[0].name} L{card[0].level} (max {card[0].maxLevel}) - have {card[0].count}, need {required_cards}")
                    if not can_upgrade:
                        log(f"Not enough cards/wildcards/books for {card[0].name}: {card[0].count}/{required_cards}. Skipping.")
                        newcardlist.append(card[0])
                        card_data.remove(card[0])
                        card = sorted(card_data, key=lambda x: x.level, reverse=False)
                        continue
                    
                    # Perform upgrade (respect gold availability)
                    card[0].count = int(card[0].count) - required_cards
                    # increment level first for cost/exp lookup
                    card[0].level = int(card[0].level) + 1
                    upgrades_performed += 1
                    log(f"Upgrading {card[0].name} -> L{card[0].level}. Remaining copies: {card[0].count}")
                    
                    # Calculate costs and experience
                    if card[0].level > 1:
                        # Use next level row for costs/exp (index card.level-1)
                        gold_cost_str = upgradeTable[card[0].level-1][1]
                        exp_gained_str = upgradeTableExp[card[0].level-1][1]
                        
                        # Handle N/A values
                        if gold_cost_str != 'N/A':
                            gold_cost = safe_to_int(gold_cost_str)
                            effective_cost = gold_cost
                            # Magic coin strategy:
                            # - If 'only_coins_level14' is True, only use coin for L13->L14 upgrades
                            # - Otherwise, use for expensive upgrades (>= 35,000) or L13+
                            if magic_items is not None and magic_items.get('magic_coins', 0) > 0 and gold_cost > 0:
                                use_coin = False
                                if magic_items.get('only_coins_level14', True):
                                    # We already incremented the card level; L14 row means we just upgraded to L14.
                                    # So coin should be used when the upgraded level is 14 (i.e., we paid the L14 cost).
                                    if card[0].level == 14:
                                        use_coin = True
                                else:
                                    if card[0].level >= 13 or gold_cost >= 35000:
                                        use_coin = True
                                if use_coin:
                                    magic_items['magic_coins'] -= 1
                                    effective_cost = 0
                                    log(f"Using Magic Coin for L{card[0].level} upgrade to waive {gold_cost} gold cost")
                            # Stop if not enough gold for this upgrade
                            if account.gold < effective_cost:
                                log(f"Insufficient gold for upgrade cost {effective_cost}. Gold remaining: {account.gold}. Stopping.")
                                break
                            total_gold_cost += effective_cost
                            account.gold = account.gold - effective_cost
                            if effective_cost > 0:
                                log(f"Gold spent: {effective_cost}. Total spent: {total_gold_cost}. Gold remaining: {account.gold}")
                        
                        if exp_gained_str != 'N/A':
                            exp_gained = safe_to_int(exp_gained_str)
                            total_exp_gained += exp_gained
                            account.exppoints = account.exppoints + exp_gained
                            log(f"Gained exp: {exp_gained}. Current exp: {account.exppoints}/{expTable[account.explevel-1][1]}")
                    
                    # Check for level up
                    if account.exppoints >= int(expTable[account.explevel-1][1]):
                        account.exppoints = account.exppoints - int(expTable[account.explevel-1][1])
                        account.explevel = account.explevel + 1
                        per_level_cumulative_gold.append({'level': account.explevel, 'cumulativeGold': total_gold_cost})
                        log(f"KING LEVEL UP! -> Level {account.explevel}. Exp carried over: {account.exppoints}. Next requirement: {expTable[account.explevel-1][1] if account.explevel-1 < len(expTable) else 'N/A'}")
                    
                    # Update card list
                    card_data = [c if c.name != card[0].name else card[0] for c in card_data]
                    card = sorted(card_data, key=lambda x: x.level, reverse=False)
                
                # Compute progress to next king level
                try:
                    next_req_exp = int(expTable[account.explevel-1][1]) if (account.explevel-1) < len(expTable) else 0
                except Exception:
                    next_req_exp = 0
                progress_pct = 0
                if next_req_exp > 0:
                    progress_pct = min(100, round((account.exppoints / next_req_exp) * 100, 2))
                
                # Store results for UI
                self.calculation_results = {
                    'currentLevel': player_data.get('expLevel'),
                    'maxAchievableLevel': account.explevel,
                    'currentExp': player_data.get('expPoints'),
                    'totalExpGained': total_exp_gained,
                    'totalGoldCost': total_gold_cost,
                    'goldRemaining': account.gold,
                    'perLevelCumulativeGold': per_level_cumulative_gold,
                    'nextLevelExpRequired': next_req_exp,
                    'expTowardsNext': account.exppoints,
                    'expProgressPercent': progress_pct,
                    'upgradesPerformed': upgrades_performed,
                    'playerName': player_data.get('name'),
                    'trophies': player_data.get('trophies')
                }
                
            else:
                raise Exception(f"Failed to fetch player data: {response.status_code}")
                
        except Exception as e:
            raise e
    
    def parse_results_from_output(self, output, player_tag):
        """Parse results from the calculation output"""
        # Use the stored results from calculate_max_level_with_existing_logic
        return getattr(self, 'calculation_results', {
            'currentLevel': 0,
            'maxAchievableLevel': 0,
            'currentExp': 0,
            'totalExpGained': 0,
            'totalGoldCost': 0,
            'upgradesPerformed': 0,
            'playerName': 'Unknown',
            'trophies': 0
        })
    
    def show_calculation_results(self, results):
        """Display calculation results"""
        # Hide loading indicator
        if hasattr(self, 'loading_label'):
            self.loading_label.destroy()
        
        # Clear previous results
        for widget in self.results_inner.winfo_children():
            widget.destroy()
        
        # Results title
        results_title = tk.Label(self.results_inner,
                                text="📊 Maximum Level Calculation Results",
                                font=('Segoe UI', 14, 'bold'),
                                bg=self.colors['bg_medium'],
                                fg=self.colors['accent'])
        results_title.pack(pady=(0, 15))
        
        # Results grid
        results_grid = tk.Frame(self.results_inner, bg=self.colors['bg_medium'])
        results_grid.pack(fill='x')
        
        # Player info
        player_info = tk.Label(results_grid,
                              text=f"Player: {results['playerName']}",
                              font=('Segoe UI', 12, 'bold'),
                              bg=self.colors['bg_medium'],
                              fg=self.colors['text_light'])
        player_info.pack(anchor='w', pady=2)
        
        # Current level
        current_level = tk.Label(results_grid,
                                text=f"Current Level: {results['currentLevel']}",
                                font=('Segoe UI', 11),
                                bg=self.colors['bg_medium'],
                                fg=self.colors['text_light'])
        current_level.pack(anchor='w', pady=2)
        
        # Max achievable level
        max_level = tk.Label(results_grid,
                            text=f"Maximum Achievable Level: {results['maxAchievableLevel']}",
                            font=('Segoe UI', 11, 'bold'),
                            bg=self.colors['bg_medium'],
                            fg=self.colors['success'])
        max_level.pack(anchor='w', pady=2)
        
        # Experience gained
        exp_gained = tk.Label(results_grid,
                             text=f"Total Experience Gained: {results['totalExpGained']:,}",
                             font=('Segoe UI', 11),
                             bg=self.colors['bg_medium'],
                             fg=self.colors['text_light'])
        exp_gained.pack(anchor='w', pady=2)
        
        # Gold cost
        gold_cost = tk.Label(results_grid,
                            text=f"Total Gold Cost: {results['totalGoldCost']:,}",
                            font=('Segoe UI', 11),
                            bg=self.colors['bg_medium'],
                            fg=self.colors['warning'])
        gold_cost.pack(anchor='w', pady=2)

        # Gold remaining
        if 'goldRemaining' in results:
            gold_remaining = tk.Label(results_grid,
                                     text=f"Gold Remaining: {results['goldRemaining']:,}",
                                     font=('Segoe UI', 11),
                                     bg=self.colors['bg_medium'],
                                     fg=self.colors['text_light'])
            gold_remaining.pack(anchor='w', pady=2)

        # Progress toward next king level
        if results.get('nextLevelExpRequired') is not None:
            prog_frame = tk.Frame(results_grid, bg=self.colors['bg_medium'])
            prog_frame.pack(fill='x', pady=(6, 4))
            tk.Label(prog_frame,
                     text=f"Progress to Next Level: {results.get('expTowardsNext',0):,} / {results.get('nextLevelExpRequired',0):,} ({results.get('expProgressPercent',0)}%)",
                     font=('Segoe UI', 11),
                     bg=self.colors['bg_medium'],
                     fg=self.colors['text_light']).pack(anchor='w')
        
        # Upgrades performed
        upgrades = tk.Label(results_grid,
                           text=f"Upgrades Performed: {results['upgradesPerformed']}",
                           font=('Segoe UI', 11),
                           bg=self.colors['bg_medium'],
                           fg=self.colors['text_light'])
        upgrades.pack(anchor='w', pady=2)
        



        # Per-level cumulative gold breakdown (if present)
        if results.get('perLevelCumulativeGold'):
            breakdown_title = tk.Label(self.results_inner,
                                       text="Per-Level Gold Breakdown (cumulative):",
                                       font=('Segoe UI', 12, 'bold'),
                                       bg=self.colors['bg_medium'],
                                       fg=self.colors['accent'])
            breakdown_title.pack(anchor='w', pady=(10, 2))

            for item in results['perLevelCumulativeGold']:
                row = tk.Label(self.results_inner,
                               text=f"Level {item['level']}: {item['cumulativeGold']:,} gold",
                               font=('Segoe UI', 10),
                           bg=self.colors['bg_medium'],
                           fg=self.colors['text_light'])
                row.pack(anchor='w')
    
    def show_calculation_error(self, error_msg):
        """Show calculation error"""
        # Hide loading indicator
        if hasattr(self, 'loading_label'):
            self.loading_label.destroy()
        
        # Clear previous results
        for widget in self.results_inner.winfo_children():
            widget.destroy()
        
        error_label = tk.Label(self.results_inner,
                              text=f"❌ Calculation Error: {error_msg}",
                              font=('Segoe UI', 11),
                              bg=self.colors['bg_medium'],
                              fg=self.colors['error'])
        error_label.pack(pady=10)
    
    def reset_validation(self):
        """Reset to validation screen"""
        self.is_validated = False
        self.debug_info = {}
        self.show_validation_screen()

def main():
    root = tk.Tk()
    app = ModernClashRoyaleUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 