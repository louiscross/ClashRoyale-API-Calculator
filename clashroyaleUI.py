import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import requests
import json
from datetime import datetime
import threading

class ModernClashRoyaleUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Clash Royale Level Calculator")
        self.root.geometry("800x600")
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
        
        # Success title
        title_label = tk.Label(self.main_frame,
                              text="✅ Validation Successful!",
                              font=('Segoe UI', 24, 'bold'),
                              bg=self.colors['bg_dark'],
                              fg=self.colors['success'])
        title_label.pack(pady=(0, 20))
        
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
        
        # Results area
        self.results_frame = tk.Frame(card_frame, bg=self.colors['bg_medium'], relief='flat', bd=0)
        self.results_frame.pack(fill='x', padx=20, pady=(0, 20))
        
        # Debug info
        debug_label = tk.Label(card_frame,
                              text="Debug Information:",
                              font=('Segoe UI', 11, 'bold'),
                              bg=self.colors['bg_medium'],
                              fg=self.colors['text_light'],
                              anchor='w')
        debug_label.pack(fill='x', padx=20, pady=(0, 5))
        
        debug_text = scrolledtext.ScrolledText(card_frame,
                                              height=8,
                                              font=('Consolas', 9),
                                              bg='#1a1a1a',
                                              fg='#00ff00',
                                              relief='flat',
                                              bd=0)
        debug_text.pack(fill='x', padx=20, pady=(0, 20))
        debug_text.insert(tk.END, json.dumps(self.debug_info, indent=2))
        debug_text.config(state='disabled')
        
        # Reset button
        reset_button = self.create_modern_button(card_frame, "Reset Validation", self.reset_validation)
        reset_button.pack(pady=20)

    def update_debug_info(self, debug_data):
        """Update debug information display"""
        self.debug_text.config(state='normal')
        self.debug_text.delete(1.0, tk.END)
        self.debug_text.insert(tk.END, json.dumps(debug_data, indent=2))
        self.debug_text.config(state='disabled')
    
    def calculate_max_level(self):
        """Calculate maximum level using existing Python logic"""
        # Get credentials from debug info (stored during validation)
        player_tag = self.debug_info.get('playerTag', '')
        auth_token = self.debug_info.get('authToken', '')
        
        # Run calculation in thread to avoid blocking UI
        thread = threading.Thread(target=self.perform_calculation, args=(player_tag, auth_token))
        thread.daemon = True
        thread.start()
    
    def perform_calculation(self, player_tag, auth_token):
        """Perform the level calculation using existing logic"""
        try:
            # Import your existing classes
            from API import Main
            import io
            import sys
            
            # Create main instance with validated credentials
            main_instance = Main(player_tag, auth_token)
            
            # Capture the output from the run method
            captured_output = io.StringIO()
            old_stdout = sys.stdout
            sys.stdout = captured_output
            
            try:
                # Call the run method but intercept the input
                # We'll need to modify the run method to accept a parameter
                # For now, let's create a modified version that calculates max level
                self.calculate_max_level_with_existing_logic(main_instance, player_tag)
                
                # Get the captured output
                output = captured_output.getvalue()
                
                # Parse the results from the output
                results = self.parse_results_from_output(output, player_tag)
                
                # Update UI on main thread
                self.root.after(0, lambda: self.show_calculation_results(results))
                
            finally:
                # Restore stdout
                sys.stdout = old_stdout
                captured_output.close()
                
        except Exception as e:
            error_msg = f"Calculation error: {str(e)}"
            self.root.after(0, lambda: self.show_calculation_error(error_msg))
    
    def calculate_max_level_with_existing_logic(self, main_instance, player_tag):
        """Use the existing API logic to calculate maximum level"""
        try:
            # Get player data using the existing method
            response = requests.get(f"https://api.clashroyale.com/v1/players/%23{player_tag}", headers=main_instance.headers)
            
            if response.status_code == 200:
                player_data = response.json()
                
                # Use existing methods from API.py
                account = main_instance.getAccount(player_data)
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
                    
                    # Check if enough cards to upgrade
                    required_cards = int(cardRequiredTable[card[0].level-1][itemRarityIndex])
                    if card[0].count < required_cards:
                        newcardlist.append(card[0])
                        card_data.remove(card[0])
                        card = sorted(card_data, key=lambda x: x.level, reverse=False)
                        continue
                    
                    # Perform upgrade (same logic as original)
                    card[0].count = int(card[0].count) - required_cards
                    card[0].level = int(card[0].level) + 1
                    upgrades_performed += 1
                    
                    # Calculate costs and experience
                    if card[0].level > 1:
                        gold_cost_str = upgradeTable[card[0].level-2][1]
                        exp_gained_str = upgradeTableExp[card[0].level-2][1]
                        
                        # Handle N/A values
                        if gold_cost_str != 'N/A':
                            gold_cost = int(gold_cost_str)
                            total_gold_cost += gold_cost
                            account.gold = account.gold - gold_cost
                        
                        if exp_gained_str != 'N/A':
                            exp_gained = int(exp_gained_str)
                            total_exp_gained += exp_gained
                            account.exppoints = account.exppoints + exp_gained
                    
                    # Check for level up
                    if account.exppoints >= int(expTable[account.explevel-1][1]):
                        account.exppoints = account.exppoints - int(expTable[account.explevel-1][1])
                        account.explevel = account.explevel + 1
                    
                    # Update card list
                    card_data = [c if c.name != card[0].name else card[0] for c in card_data]
                    card = sorted(card_data, key=lambda x: x.level, reverse=False)
                
                # Store results for UI
                self.calculation_results = {
                    'currentLevel': player_data.get('expLevel'),
                    'maxAchievableLevel': account.explevel,
                    'currentExp': player_data.get('expPoints'),
                    'totalExpGained': total_exp_gained,
                    'totalGoldCost': total_gold_cost,
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
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        # Results title
        results_title = tk.Label(self.results_frame,
                                text="📊 Maximum Level Calculation Results",
                                font=('Segoe UI', 14, 'bold'),
                                bg=self.colors['bg_medium'],
                                fg=self.colors['accent'])
        results_title.pack(pady=(0, 15))
        
        # Results grid
        results_grid = tk.Frame(self.results_frame, bg=self.colors['bg_medium'])
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
        
        # Upgrades performed
        upgrades = tk.Label(results_grid,
                           text=f"Upgrades Performed: {results['upgradesPerformed']}",
                           font=('Segoe UI', 11),
                           bg=self.colors['bg_medium'],
                           fg=self.colors['text_light'])
        upgrades.pack(anchor='w', pady=2)
        
        # Trophies
        trophies = tk.Label(results_grid,
                           text=f"Current Trophies: {results['trophies']:,}",
                           font=('Segoe UI', 11),
                           bg=self.colors['bg_medium'],
                           fg=self.colors['text_light'])
        trophies.pack(anchor='w', pady=2)
    
    def show_calculation_error(self, error_msg):
        """Show calculation error"""
        # Hide loading indicator
        if hasattr(self, 'loading_label'):
            self.loading_label.destroy()
        
        # Clear previous results
        for widget in self.results_frame.winfo_children():
            widget.destroy()
        
        error_label = tk.Label(self.results_frame,
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