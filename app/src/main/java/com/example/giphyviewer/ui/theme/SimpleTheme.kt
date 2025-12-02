package com.example.giphyviewer.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color

private val DarkColorScheme = darkColorScheme(
    primary = Color(0xFFFFA726),
    secondary = Color(0xFFFF7043),
    tertiary = Color(0xFFFFCA28),
    background = Color(0xFF121212),
    surface = Color(0xFF1E1B16),
    onPrimary = Color.Black,
    onSecondary = Color.Black,
    onTertiary = Color.Black,
    onBackground = Color.White,
    onSurface = Color(0xFFE0E0E0),
    primaryContainer = Color(0xFF5D4037),
    secondaryContainer = Color(0xFF8D6E63)
)

private val LightColorScheme = lightColorScheme(
    primary = Color(0xFFF57C00),
    secondary = Color(0xFFFF9800),
    tertiary = Color(0xFFFFB300),
    background = Color(0xFFFFF8E1),
    surface = Color(0xFFFFF3E0),
    onPrimary = Color.White,
    onSecondary = Color.Black,
    onTertiary = Color.Black,
    onBackground = Color(0xFF212121),
    onSurface = Color(0xFF424242),
    primaryContainer = Color(0xFFFFCC80),
    secondaryContainer = Color(0xFFFFE0B2)
)

@Composable
fun SimpleGiphyTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    content: @Composable () -> Unit
) {
    val colorScheme = if (darkTheme) DarkColorScheme else LightColorScheme

    MaterialTheme(
        colorScheme = colorScheme,
        content = content
    )
}