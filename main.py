import pandas as pd
from Bar import *
from Real_time_Student_Ranking_Monitoring_System_QT import *
import sys

def get_score(data):
    return data['成绩'].tolist()

def get_name(data):
    return data['姓名'].tolist()

def rank():
    global data, file_name
    data['排名'] = data['成绩'].rank(ascending=False, method='min').astype(int)
    data.sort_values(by=['排名', '序号'], ascending=[True, True], inplace=True)
    data.to_excel(file_name, index=False)
    return data['成绩'].tolist()

def change_val(name, value):
    global data, file_name
    index = data[data['姓名'] == name].index
    if not index.empty:
        current_score = data.loc[index, '成绩'].values[0]
        data.loc[index, '成绩'] = current_score + value
        data.to_excel(file_name, index=False)
    else:
        print(f"找不到姓名为 {name} 的学生。")

def set_mycss(html_file):

    css_style = """
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
            border: 1px solid #ddd;
            font-size: 0.9em;
            font-family: Arial, sans-serif;
        }
        table th, table td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        table th {
            background-color: #f2f2f2;
            color: #333;
            font-weight: bold;
        }
        table tbody tr:nth-of-type(even) {
            background-color: #f9f9f9;
        }
        table tbody tr:last-of-type {
            border-bottom: 2px solid #333;
        }
    </style>
    """
    with open(html_file, "r") as file:
        html_content = file.read()
    # 构建完整的 HTML 结构
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>HTML Table</title>
        {css_style}
    </head>
    <body>
    {html_content}
    </body>
    </html>
    """

    # 将带有额外 CSS 样式的 HTML 内容写回到文件中
    with open(html_file, "w") as file:
        file.write(html_content)
    return html_content


def convert_data(data):
    data = data.to_html(index=False)
    with open("data.html", "w") as file:
        file.write(data)
    data = set_mycss("data.html")
    # data = read_html_content("data.html")
    return data

def read_html_content(html_file):
    with open(html_file, "r") as file:
        html_content = file.read()
    return html_content

def add_button(value):
    global ui, data
    current_name = ui.nameList.currentText()
    change_val(current_name, value)
    rank()
    render_new(get_name(data), get_score(data))
    ui.table_label.setHtml(convert_data(data))
    ui.label_2.setHtml(read_html_content("combined_chart.html"))

def start_ui():
    global ui, data
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui.setupUi(MainWindow)
    ui.nameList.addItems(names)
    ui.nameList.setCurrentText(names[0])
    ui.addButton.clicked.connect(lambda: add_button(1))
    ui.reduceButton.clicked.connect(lambda: add_button(-1))
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    file_name = "上午.xlsx"
    data = pd.read_excel(file_name)
    names = get_name(data)
    score = get_score(data)
    ui = Ui_MainWindow()
    start_ui()




