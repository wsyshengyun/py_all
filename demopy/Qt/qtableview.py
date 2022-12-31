# coding:utf8
from PyQt5.QtWidgets import QTableView


def create_tableview():
    view = QTableview()

    #Prepare view
    #    oldh, oldv = view.horizontalHeader(), view.verticalHeader()
    #    oldh.setParent(form), oldv.setParent(form) #Save old headers for some reason
    MultiIndexHeaderView(Qt.Horizontal, view)
    MultiIndexHeaderView(Qt.Vertical, view)
    view.horizontalHeader().setMovable(True) #reorder DataFrame columns manually



    # Set data
    view.setModel(DataFrameModel(df))
    view.resizeColumnsToContents()
    view.resizeRowsToContents()


    #Set sorting enabled (after setting model)
    view.setSortingEnabled(True)
