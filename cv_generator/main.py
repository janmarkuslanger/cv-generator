from generate_pdf import generate_pdf
from implementations import Demo
from output import Output

demo = Demo()

output = Output(language='de')

generate_pdf(demo, output)