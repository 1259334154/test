import pandas as pd
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def page_4():
    # st.write('到时候设置成固定文件')
    # st.set_page_config(page_icon="🌴", page_title="Tabulator", layout="wide")

    df = pd.read_csv('./all.csv', encoding="gbk")


    def draw_table(df, height, width):  # css画表
        columns = df.columns
        column_selection = []

        # 列

        table_data = df.to_dict(orient="records")
        column_setting = []
        for y in range(df.shape[1]):
            column_setting.append(
                {"title": columns[y],
                 "field": columns[y],
                 "width": 140,
                 "sorter": "string",
                 "hozAlign": "center",
                 "headerFilter": "input",
                 "editor": "input"}
            )

        components.html("""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>test</title>
            <link href="https://unpkg.com/tabulator-tables@4.8.1/dist/css/tabulator_modern.min.css" rel="stylesheet">
            <script type="text/javascript" src="https://unpkg.com/tabulator-tables@4.8.1/dist/js/tabulator.min.js"></script>
            <script type="text/javascript" src="https://moment.github.io/luxon/global/luxon.min.js"></script>
            <script type="text/javascript" src="https://oss.sheetjs.com/sheetjs/xlsx.full.min.js"></script>
        </head><body> 
            <div style="margin-left:30%;">""" + "".join(column_selection) +
                        """
            </div><script type="text/javascript">
                var fieldEl = document.getElementById("filter-field");
                var typeEl = document.getElementById("filter-type");
                var valueEl = document.getElementById("filter-value");
                function customFilter(data){
                    return data.car && data.rating < 3;
                }function updateFilter(){
                  var filterVal = fieldEl.options[fieldEl.selectedIndex].value;
                  var typeVal = typeEl.options[typeEl.selectedIndex].value;
                  var filter = filterVal == "function" ? customFilter : filterVal;
                  if(filterVal == "function" ){
                    typeEl.disabled = true;
                    valueEl.disabled = true;
                  }else{
                    typeEl.disabled = false;
                    valueEl.disabled = false;
                  }
                  if(filterVal){
                    table.setFilter(filter,typeVal, valueEl.value);
                  }
                }
                document.getElementById("filter-field").addEventListener("change", updateFilter);
                document.getElementById("filter-type").addEventListener("change", updateFilter);
                document.getElementById("filter-value").addEventListener("keyup", updateFilter);
                document.getElementById("filter-clear").addEventListener("click", function(){
                  fieldEl.value = "";
                  typeEl.value = "=";
                  valueEl.value = "";
                  table.clearFilter();
                });
            </script>
            <script type="text/javascript">
                var table = new Tabulator("#example-table", {
                    ajaxURL:"http://www.getmydata.com/now",
                });
                document.getElementById("download-csv").addEventListener("click", function(){
                    table.download("csv", "data.csv");
                });
                document.getElementById("download-xlsx").addEventListener("click", function(){
                    table.download("xlsx", "data.xlsx", {sheetName:"My Data"});
                });
                document.getElementById("download-html").addEventListener("click", function(){
                    table.download("html", "data.html", {style:true});
                });
            </script><div id="players" style="margin-left:16%;"></div>""" +
                        """<script type="text/javascript">
                var tabledata = [""" + ','.join(list(map(str, table_data))) + """];""" +
                        """var table = new Tabulator("#players", {
                    height: '520px',
                    data: tabledata,
                    layout: "fitDataTable",
                    autoResize:false,
                    resizableRows:false,
                    movableRows:false,
                    resizableColumns:false,
                    pagination: "local",
                    paginationSize:2300,
                    tooltips: false,
                    columns: [""" + ','.join(list(map(str, column_setting))) + """],});</script></body></html>""",
                        height=height, width=width)

    draw_table(df, 550, 2050)
