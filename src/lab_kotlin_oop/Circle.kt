package lab_kotlin_oop

import kotlin.math.PI

class Circle(
    private val radius: Double,
    private val colour: Color
) : Shape() {

    override val name: String = "Круг"

    override fun area(): Double = PI * radius * radius

    override fun repr(): String {
        return String.format(
            "Имя: %s, Радиус: %.2f, Цвет: %s, Площадь: %.2f",
            name, radius, colour.colorName, area()
        )
    }
}