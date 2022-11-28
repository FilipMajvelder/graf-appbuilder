
from flask_appbuilder.charts.views import DirectByChartView
from flask_appbuilder.models.sqla.interface import SQLAInterface
from

from . import appbuilder, db

class GrafCisel(DirectByChartView):
    datamodel = SQLAInterface(Cisla)
    chart_title = 'Cislo'

    definitions = [
    {
        'label': 'Cislo',
        'group': 'id',
        'series': ['cislo']
    }
]

db.create_all()

appbuilder.add_view(
    GrafCisel, "Cislo", icon="fa-chart"
)

appbuilder.add_view(GrafCisel, "Show Country Chart", icon="fa-dashboard", category="Statistics")


