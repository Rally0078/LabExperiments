#include <iostream>
#include <vector>
#include <sciplot/sciplot.hpp>
#include <rapidcsv.h>

using namespace sciplot;

int main(void) {
    rapidcsv::Document calib("calib.csv");
    std::vector<double> current = calib.GetColumn<double>("Calib");
    std::vector<double> field = calib.GetColumn<double>("Field");

    Plot2D plot;
    plot.xlabel("Current (A)");
    plot.ylabel("Magnetic Field (G)");
    plot.xrange(0.0, 5.0);
    plot.yrange(0.0, 7000);
    plot.legend()
        .atOutsideBottom()
        .displayHorizontal()
        .displayExpandWidthBy(2);
    plot.drawCurve(current, field).label("");
    Figure fig = {{plot}};
    fig.title(" Calibration: Magnetic field vs Coil Current");
    fig.palette("dark2");
    fig.get(0,0).grid().show();
    Canvas canvas = {{fig}};
    canvas.size(1024, 768);
    canvas.title("Magnetic field Calibration Plot");
    canvas.show();
    canvas.save("calib.pdf");

    return 0;
}

