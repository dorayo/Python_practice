#!/usr/local/bin/python3
# coding: utf-8
# pdf_watermark.py

import os
from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def create_watermark(content):
    """创建PDF水印模板
    """

    packet = io.BytesIO()
    # 使用reportlab来创建一个PDF文件来作为一个水印文件
    c = canvas.Canvas(packet, pagesize=letter)
    c.setFont('Courier', 10)

    # 设置水印文件
    c.saveState()
    c.translate(300, 15)
    # 水印文字
    c.drawCentredString(0, 0, content)
    c.restoreState()
    # 保存水印文件
    c.save()

    #move to the beginning of the StringIO buffer
    packet.seek(0)
    pdf_watermark = PdfFileReader(packet)
    return pdf_watermark

def add_watermark(pdf_file, pdf_watermark, output_dir='output'):
    """给指定PDF文件文件加上水印
    pdf_file - 要加水印的源PDF文件
    pdf_watermark - PDF水印模板
    """

    # read your existing PDF
    existing_pdf = PdfFileReader(open(pdf_file, "rb"), strict=False)
    output = PdfFileWriter()
    # add the "watermark" (which is the pdf_watermark) on the existing page
    pageNum = existing_pdf.getNumPages()
    for i in range(pageNum):
        page = existing_pdf.getPage(i)
        page.mergePage(pdf_watermark.getPage(0))
        output.addPage(page)


    # 最后输出文件
    output_stream = open(os.path.join(output_dir, os.path.basename(pdf_file)), 'wb')
    output.write(output_stream)
    output_stream.close()

    return True

if __name__ == '__main__':
    # 创建水印文件
    pdf_watermark = create_watermark("Dorayo's Resume - http://dorayo.com")
    add_watermark("./Resume4Dorayo.pdf", pdf_watermark)

