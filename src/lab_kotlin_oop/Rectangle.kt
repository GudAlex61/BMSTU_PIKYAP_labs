package lab_kotlin_oop

class Rectangle(
    private val width: Double,
    private val height: Double,
    private val color: Color
) : Shape() {

    override val name: String = "Прямоугольник"

    override fun area(): Double = width * height

    override fun repr(): String {
        return String.format(
            "Имя: %s, Ширина: %.2f, Высота: %.2f, Цвет: %s, Площадь: %.2f",
            name, width, height, color.colorName, area()
        )
    }
}