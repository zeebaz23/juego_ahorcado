# 🏆 Juego de Ahorcado

## 📖 Descripción

**Ahorcado** es un juego clásico de palabras en el que un jugador debe adivinar una palabra oculta antes de que se
agoten sus intentos.

## 📌 Reglas del Juego

1. Se selecciona una palabra secreta al azar.
2. El jugador intenta adivinar la palabra, **proponiendo una letra por turno**.
3. Si la letra está en la palabra, se revela en su posición correspondiente.
4. Si la letra no está en la palabra, se **pierde un intento**.
5. El juego continúa hasta que el jugador:
    - Adivina completamente la palabra (**gana**).
    - Agota todos sus intentos (**pierde**).

## 🎯 Objetivo

Descubrir la palabra oculta antes de quedarse sin intentos.

## 🛠️ Tecnologías Utilizadas

- Lenguaje: **Python**
- Conceptos aplicados: **Manejo de cadenas, estructuras de control, validación de entrada**

## 🚀 Cómo Jugar

1. Ejecuta el script en Python:
   ```bash
   python app.py
https://viewer.diagrams.net/?tags=%7B%7D&lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=diagramaa.drawio&dark=auto#R%3Cmxfile%3E%3Cdiagram%20id%3D%22C5RBs43oDa-KdzZeNtuy%22%20name%3D%22Page-1%22%3E7ZxbU9s6EMc%2FTWY4D3R8SUx4JFBoOWmHlrb0PGWErTgqipUjKyTh03dly7dIuVGcTMEzzBStJdnW7y9pd%2BXScs%2FH8yuOJqNPLMC05VjBvOVetBzHdtwO%2FCMti9Tidb3UEHISqEqF4ZY8YWW0lHVKAhxXKgrGqCCTqtFnUYR9UbEhztmsWm3IaPWuExRizXDrI6pb70ggRqm165wU9g%2BYhKPszrZ3ml4Zo6yyepN4hAI2K5nc9y33nDMm0t%2FG83NM5eBl43L3cXFH%2Bw%2Fe1fWX%2BH%2F0vffvt88%2FjtPOLndpkr8Cx5F4dtdPD8PLDz%2Fav35Obi6%2FzKyrs%2FvrY9XEekR0qsbreopDpl5YLLJRjGdkTFEEpd6QReJWXYEx6CFKwgh%2B9%2BHhMAfDI%2BaCAIAzdUGwCVj9EaFBHy3YVL5CLJD%2FkJV6I8bJE3SLKFyywQCXuVBacrxKjVvZEswWWDmOoc5NNi52buqjWKg6PqMUTWJynzywrDJGPCRRjwnBxllHbBoFOFClHHRSEJw95NKR7bekoajJ0cDzkhYVnSvMxljwBVTJrlqKhpppme5mhWwdV9lGJcm6J46aLmqqhHnX%2Bd2%2BwtRCUQhjkN8u70vdzm7r97M9w%2F0cr3o7RIF7hATuyVGMyyKEX0pvWpgSae4gU1uT6WAQkCHxp1QgaHiWqJVrsoWRFyWJUjwUKwUaT5BPorCf1LloF5av6tWliUHbIU3EMSJBgKNEPAIJlOpLKmbCSCSSsen04AdG8Nx612l14IHOoWwXZfiR1bk4ZxE8PiKJoDCId4algA1SWzuLN0ttUUW4SVrLqMvKqjBeAxT1f8wfPwYfup%2F7d9TDH79%2FWlwb1h0J1PcJixAnLCV6UTK8NrJrVpyRGFP16wqu20piJf%2BOc2D%2BpgmNAvJIIhQ9oRT%2FWVFu6L8k%2FZPugem7BvowRvBOLB5wDFifYETiVAZy8Br%2BL8nfttr7E4Dx%2BdqaADTElCTephoO2%2BiJbeA%2FBpKyuwz4N6mHi2NbE4Wri8I1CICie0xvWEwE7Epg42ndJWEcak%2B33S39xW5NUDsaVHYPcxpz09w%2B%2BgeqHrccL0zH5FVO8%2FpQH3oF1ydwxrrYxTXEr3hDr22p9va4VBtJ67N6MAglacQHEwRLItdBv95QrAbCp1su2%2FX54o6GGF5TRteAOCaDEVrkK7iG%2Bp4x2rDekjVM5wOz9jTUAMSfUlTapCeYj8HFeVubdA2w2wcPsvUou5jYgpNpNGTNhP4jxt6hHTFbz6QpD4wfUbgDypOjy6ApgaHp9ORYdS4a4tsSPz20Q9bVgI9ZoCZ1kRM%2FMqTHlxXwmUGI3YDfDry77XFMbeBPNPAkIj5J%2FHCgE%2Bh%2BeLNd78C3vUffzHzIpQNedwKy4kjWajVHsq2XOpLtWGq1zYI1wyJgdx1dJHnF3c5kO52%2F6ExW34hUPkAl7pWDIZMBr9bB2Ljo5JP6T85mjRKrbR1y9OMZjd5bz87vjtVw5GrEWld23tFTtoMB%2BIxhkcfT4%2F1mCj%2BLtbflLlHfFF59FvP2crY1AO4efI3WE3kaPRwFZ%2FIDSiixSTLUG7yoqsvlT%2FljXoC%2BLgnN1nochDjzNzG9Z7P3haGXGOBCJpOd3bOYTbmPNznyjgUOaYi34SofdxtvT8qq7H211QNxTJEgj%2BU%2B1jp2NywJvLJu3e6SU3fqVLtIX1i1KoShddRpb%2BgoHZHNHR0vdeQu9cOGwxhXuniG02hOV%2Bm6XXMq2IQ4yyHOhrh39bRaHeLYS1o4MeQ5bFPI0V5SzV8d4pjVqkfkg0GSVX1DIc4Gya2Z5jt9fmqUWF2pNEc%2FGRkMJhA7yGwLrsJNDkQautvTNX1cule6hsyERu%2BVB7A1YDV9NWrC%2BgIBrPnxTjWqzUlXncANQc6eV2lHI55Fsekm%2FCbzFTWQtu1DL9mGnGOesMi35VW4mx16V96m70f3y3v1B6Q%2BiuRhZrAO%2FJs92HwWbdM3pPulracjm627VuSmj0r3i1z%2FLkn7qLT5BO1FgmnTR6X7Ze1ptMoZYhiUEQtZhGg5TVxNfhV1%2BiwJo2QU9QsLsVD5ODQVrBqv4TkRP2VzAJCW%2FitduZirnpPCIitE8L5po7ZjZwbZ7th6Z1luZilaJ6VK8xuQMYybTDqW%2FpfWUo75BbPdWRKqnO7eSSdbp69XiACKxR85SFNrxZ%2BKcN%2F%2FBg%3D%3D%3C%2Fdiagram%3E%3C%2Fmxfile%3E
