import curses

def main(stdscr):
    # Инициализация цветов
    curses.start_color()
    curses.use_default_colors()

    # Преобразование HEX в RGB
    # #EBAB34 -> RGB(235, 171, 52)
    r, g, b = 235, 171, 52

    # Создаем цвет и цветовую пару
    if curses.can_change_color():
        # Создаем пользовательский цвет (только если терминал поддерживает)
        curses.init_color(100, r * 1000 // 255, g * 1000 // 255, b * 1000 // 255)
        curses.init_pair(1, curses.COLOR_WHITE, 100)  # Белый текст на вашем фоне
    else:
        # Используем ближайший доступный цвет
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_YELLOW)

    # Очищаем экран
    stdscr.clear()

    # Включаем цветовую пару
    stdscr.attron(curses.color_pair(1))

    # Выводим текст
    stdscr.addstr(5, 5, "Текст на фоне #EBAB34")
    stdscr.addstr(7, 5, "Text on #ebab34 background")

    # Отключаем цветовую пару
    stdscr.attroff(curses.color_pair(1))

    # Обновляем экран
    stdscr.refresh()
    while True:
        continue

    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
