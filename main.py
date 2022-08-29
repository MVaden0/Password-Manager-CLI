from koios.koios import *

koios = Koios([
    Text(text="Hey there!", formatting=Formatting(color='green')),
    Question(
        'Enter your password.'
    ),
    Select(
        'What information will you like to perform?',
        [
            'Get information',
            'Set information',
            'Create new file'
        ]
    )
])

koios.question()

print(koios.get_answers())


