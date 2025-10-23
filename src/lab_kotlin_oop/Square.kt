package lab_kotlin_oop

class Square(
    private val side: Double,
    private val color: Color
) : Shape() {

    override val name: String = "Квадрат"

    override fun area(): Double = side * side

    override fun repr(): String {
        return String.format(
            "Имя: %s, Сторона: %.2f, Цвет: %s, Площадь: %.2f",
            name, side, color.colorName, area()
        )
    }
}