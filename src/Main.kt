import lab_kotlin_oop.*

fun main() {
    val rectangle = Rectangle(5.0, 3.0, Color("синий"))
    val circle = Circle(4.0, Color("красный"))
    val square = Square(5.0, Color("зеленый"))

    println("=== Геометрические фигуры ===")
    println(rectangle.repr())
    println(circle.repr())
    println(square.repr())

    println("\n=== Дополнительная информация ===")
    val shapes = listOf(rectangle, circle, square)
    shapes.forEach { shape ->
        println("${shape.name}: площадь = ${"%.2f".format(shape.area())}")
    }
}