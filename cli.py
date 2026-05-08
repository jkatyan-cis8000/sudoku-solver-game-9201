import sys
from game import SudokuGame


def print_help():
    print("\nSudoku Game Commands:")
    print("  move <row> <col> <value> - Enter a number (rows/cols: 0-8, value: 1-9)")
    print("  check                    - Check current mistake count")
    print("  hint <row> <col>         - Get a hint for a cell")
    print("  solve                    - Show the solution")
    print("  new <difficulty>         - Start new game (easy/medium/hard/expert)")
    print("  quit                     - Exit the game")
    print("  help                     - Show this help message")
    print("  display                  - Show the current board")


def parse_command(input_str):
    parts = input_str.strip().split()
    if not parts:
        return None, []
    
    command = parts[0].lower()
    args = parts[1:]
    return command, args


def main():
    print("=== Sudoku Game ===")
    print("Enter 'help' for commands or 'quit' to exit\n")
    
    game = SudokuGame('medium')
    game.display()
    
    while True:
        try:
            user_input = input("\n> ").strip()
        except EOFError:
            print("\nGoodbye!")
            break
        
        if not user_input:
            continue
        
        command, args = parse_command(user_input)
        
        if command == 'quit':
            print("Thanks for playing!")
            break
        
        elif command == 'help':
            print_help()
        
        elif command == 'display':
            game.display()
        
        elif command == 'check':
            mistakes = game.check_mistakes()
            print(f"Mistakes: {mistakes}")
        
        elif command == 'new':
            if args:
                difficulty = args[0].lower()
                if difficulty in ['easy', 'medium', 'hard', 'expert']:
                    game = SudokuGame(difficulty)
                    game.display()
                else:
                    print("Invalid difficulty. Use: easy, medium, hard, expert")
            else:
                print("Usage: new <difficulty>")
        
        elif command == 'solve':
            game.solve()
            game.display()
            print("Puzzle solved!")
        
        elif command == 'hint':
            if len(args) == 2:
                try:
                    row = int(args[0])
                    col = int(args[1])
                    hint = game.get_hint(row, col)
                    if hint is not None:
                        print(f"Hint: Cell [{row},{col}] should be {hint}")
                    else:
                        print("Invalid cell coordinates")
                except ValueError:
                    print("Row and column must be numbers")
            else:
                print("Usage: hint <row> <col>")
        
        elif command == 'move':
            if len(args) == 3:
                try:
                    row = int(args[0])
                    col = int(args[1])
                    value = int(args[2])
                    success, error = game.make_move(row, col, value)
                    if success:
                        game.display()
                        if game.is_solved():
                            print("\nCongratulations! You solved the puzzle!")
                    else:
                        print(error)
                except ValueError:
                    print("Row, column, and value must be numbers")
            else:
                print("Usage: move <row> <col> <value>")
        
        else:
            print(f"Unknown command: {command}. Enter 'help' for commands.")


if __name__ == "__main__":
    main()
