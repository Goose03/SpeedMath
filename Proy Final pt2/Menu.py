from blessed import Terminal

term = Terminal()

def draw_menu(items, selected):
    # Render prompt
    for idx, item in enumerate(items):
        color = term.cyan2 if idx == selected else term.normal
        print(f'{color}{item}{term.normal}')

def menu_seleccion(items, prompt=None):
    index = 0
    draw_menu(items, index)
    with term.cbreak(), term.hidden_cursor():
        while True:
            print(term.move_up(len(items)), end='')
            draw_menu(items, index)
            key = term.inkey(2)
            if key.name == 'KEY_UP':
                index = (index - 1) % len(items)
            elif key.name == 'KEY_DOWN':
                index = (index + 1) % len(items)
            elif key.name == 'KEY_ENTER':
                return items[index]

def main():
    pass

if __name__ == '__main__':
    main()
