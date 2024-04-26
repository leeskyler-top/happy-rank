from pyecharts.charts import Map, Bar, Line, Pie
import pyecharts.options as opts

def set_flex(html_file):
    # 读取生成的 HTML 文件内容
    with open(html_file, "r") as file:
        html_content = file.read()

    # 添加额外的 CSS 样式到 HTML 内容中
    css_style = """
        <style>
            * {
                margin: 0;
                padding: 0;
            }

            html {
                height: 100%;
            }

            body {
                width: 100%;
                height: 100%;
                display: flex;
                align-items: center;
                justify-content: center;
                background-image: url(http://127.0.0.1/img/Launch.svg);
                background-repeat: no-repeat;
                background-size: 40%;
                background-position: center;

                
            }
        </style>
    """

    # 将 CSS 样式添加到 HTML 内容中
    html_content_with_css = html_content.replace("</head>", f"{css_style}</head>")

    # 将带有额外 CSS 样式的 HTML 内容写回到文件中
    with open(html_file, "w") as file:
        file.write(html_content_with_css)
def render_new(name, value):
    bar = Bar(init_opts=opts.InitOpts(animation_opts=opts.AnimationOpts(animation_duration=1000,  animation_delay=300 ,animation_easing="cubicOut")))
    bar.add_xaxis(name)
    bar.add_yaxis("分数", value)
    bar.extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} 分")
        )
    )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markline_opts=opts.MarkLineOpts(data=[
            opts.MarkLineItem(type_="average"),
        ]),
        markpoint_opts=opts.MarkPointOpts(data=[
            opts.MarkPointItem(type_="max"),
            opts.MarkPointItem(type_="min")
        ]),
        itemstyle_opts={
            "color": {
                "type": 'linear',
                "x": 0,
                "y": 0,
                "x2": 0,
                "y2": 1,
                "colorStops": [{
                    "offset": 0, "color": '#4c3a86'
                }, {
                    "offset": 1, "color": '#B1A7F2'
                }],
            },
        }
    )

    bar.set_global_opts(
        title_opts=opts.TitleOpts(title="分数排名可视化"),
        yaxis_opts=opts.AxisOpts(name="分数", axislabel_opts=opts.LabelOpts(formatter="{value} 分")),
        # datazoom_opts=opts.DataZoomOpts()
    )

    bar.render("combined_chart.html")
    set_flex("combined_chart.html")
