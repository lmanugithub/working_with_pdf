from os import write
import PyPDF2
import sys


def rotate(file_to_open, output):
    with open(file_to_open, 'rb') as file:  # rb read the binary
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
        writer = PyPDF2.PdfFileWriter()

        for i in range(reader.getNumPages()):

            page = reader.getPage(i)
            page.rotateCounterClockwise(270)

            writer.addPage(page)
            with open(f'./files_rotateds/{output}', 'wb') as new_file:
                writer.write(new_file)

if __name__ == '__main__':
    inputs = sys.argv[1]
    output = sys.argv[2]
    rotate(inputs, output)