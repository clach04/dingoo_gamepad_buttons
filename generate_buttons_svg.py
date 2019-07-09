#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
#

import os
import sys


def doit():
    str_template_round = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.0"
width="500" height="500"
id="svg2"
sodipodi:docname="%(button)s.svg"
sodipodi:version="0.32" inkscape:version="0.46"
inkscape:output_extension="org.inkscape.output.svg.inkscape"
>

  <path d="M 469.50507,249.99999 C 469.52984,371.24681 371.24682,469.54991 250,469.54991 C 128.75319,469.54991 30.470164,371.24681 30.494934,249.99999 C 30.470164,128.75319 128.75319,30.450087 250,30.450087 C 371.24682,30.450087 469.52984,128.75319 469.50507,249.99999 L 469.50507,249.99999 z"
      style="fill: rgb(255, 255, 255); fill-opacity: 0;
      stroke: rgb(0, 0, 0); stroke-width: 15;
      display: inline;" id="button"/>

  <text xml:space="preserve" style="font-size: 368.374px; font-style: normal; font-weight: normal;
    fill: rgb(0, 0, 0); fill-opacity: 1;
    stroke: none; stroke-width: 1px; stroke-linecap: butt; stroke-linejoin: miter; stroke-opacity: 1; font-family: Bitstream Vera Sans;" x="122.198" y="394.627" id="button_text" transform="scale(1.03315, 0.967914)">
    <tspan sodipodi:role="line" id="tspan4333" x="122.198" y="394.627">%(button)s</tspan>
  </text>

</svg>
"""

    str_template_start = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.0"
id="svg2"
sodipodi:docname="%(button)s.svg"
sodipodi:version="0.32" inkscape:version="0.46"
inkscape:output_extension="org.inkscape.output.svg.inkscape">
  
  <g inkscape:label="Layer 1" inkscape:groupmode="layer" id="button_group" transform="translate(-2.5, -2.5)">
    <rect
        style="opacity: 1;
        fill: rgb(255, 255, 255);
        fill-opacity: 1;
        stroke: rgb(0, 0, 0); stroke-width: 15; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;" id="button"
        width="550" height="160" x="10" y="10" ry="80"/>
        
    <text xml:space="preserve" style="font-size: 126.065px; font-style: normal; font-weight: normal;
        fill: rgb(0, 0, 0); fill-opacity: 1;
        stroke: none; stroke-width: 1px; stroke-linecap: butt; stroke-linejoin: miter; stroke-opacity: 1; font-family: Bitstream Vera Sans;"
        x="191.47" y="134.057" id="button_text" transform="scale(0.97143, 1.02941)">

        <tspan sodipodi:role="line" id="button_text_tspan" x="70" y="134.057">%(button)s</tspan>
    </text>
    
  </g>
</svg>
"""

    str_template_dpad = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.0"
id="svg2"
sodipodi:docname="%(button)s.svg"
sodipodi:version="0.32" inkscape:version="0.46"
inkscape:output_extension="org.inkscape.output.svg.inkscape">
  
    <g id="dpad_group"
        transform="%(highlight)s"
    >
      <rect ry="16.883118" y="0" x="200" height="600" width="200" id="dpad_left_right_box" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(249, 249, 249); stroke-width: 0pt; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"/>
      <rect transform="matrix(0, 1, -1, 0, 0, 0)" ry="16.883118" y="-600" x="200" height="600" width="200" id="dpad_up_down_box" style="fill: rgb(0, 0, 0); fill-opacity: 1; stroke: rgb(249, 249, 249); stroke-width: 0pt; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"/>
      <rect transform="matrix(0, 1, -1, 0, 0, 0)" ry="16.883118" y="-580" x="220" height="560" width="160" id="dpad_down_fill" style="fill: rgb(230, 230, 230); fill-opacity: 1; stroke: rgb(249, 249, 249); stroke-width: 0pt; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"/>
      <rect transform="matrix(0, 1, -1, 0, 0, 0)" ry="11.607143" y="-240" x="220" height="220" width="160" id="dpad_up_fill_red" style="fill: rgb(232, 70, 70); fill-opacity: 1; stroke: rgb(249, 249, 249); stroke-width: 0pt; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"/>
      <rect ry="16.883118" y="20" x="220" height="560" width="160" id="dpad_left_right_fill" style="fill: rgb(230, 230, 230); fill-opacity: 1; stroke: rgb(249, 249, 249); stroke-width: 0pt; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"/>
      <path transform="translate(180, 80)" d="M 180,220 A 60,60 0 1 1 60,220 A 60,60 0 1 1 180,220 z" sodipodi:ry="60" sodipodi:rx="60" sodipodi:cy="220" sodipodi:cx="120" id="dpad_center_circle" style="fill: rgb(179, 179, 179); fill-opacity: 1; stroke: rgb(128, 128, 128); stroke-width: 8; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;" sodipodi:type="arc"/>
      <path sodipodi:nodetypes="cccc" id="dpad_right_triangle" d="M 299.94534,39.9366 L 359.89068,119.99999 L 240,120 L 299.94534,39.9366 z" style="fill: rgb(179, 179, 179); fill-opacity: 1; stroke: rgb(128, 128, 128); stroke-width: 8; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"/>
      <path sodipodi:nodetypes="cccc" id="dpad_left_triangle" d="M 300,560 L 359.94534,479.93661 L 240.05466,479.9366 L 300,560 z" style="fill: rgb(179, 179, 179); fill-opacity: 1; stroke: rgb(128, 128, 128); stroke-width: 8; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"/>
      <path sodipodi:nodetypes="cccc" id="dpad_down_triangle" d="M 560.0634,299.94534 L 480.00001,359.89068 L 480,240 L 560.0634,299.94534 z" style="fill: rgb(179, 179, 179); fill-opacity: 1; stroke: rgb(128, 128, 128); stroke-width: 8; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"/>
      <path sodipodi:nodetypes="cccc" id="dpad_up_triangle" d="M 39.93661,299.94534 L 120,240 L 120.00001,359.89068 L 39.93661,299.94534 z" style="fill: rgb(195, 51, 51); fill-opacity: 1; stroke: rgb(118, 47, 47); stroke-width: 8; stroke-miterlimit: 4; stroke-dasharray: none; stroke-opacity: 1;"/>
    </g>

</svg>
"""

    str_template_shoulder = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:svg="http://www.w3.org/2000/svg" xmlns="http://www.w3.org/2000/svg" xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd" xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape" version="1.0"
id="svg2"
sodipodi:docname="%(button)s.svg"
sodipodi:version="0.32" inkscape:version="0.46"
inkscape:output_extension="org.inkscape.output.svg.inkscape">
  
  <g inkscape:label="Layer 1" inkscape:groupmode="layer" id="shoulder_group" transform="translate(-3.00381, -1.15209)">
    <path style="fill: rgb(235, 236, 236); fill-opacity: 1; stroke: rgb(0, 0, 0); stroke-width: 14.2164; stroke-miterlimit: 4; stroke-opacity: 1;" d="M 329.88424,8.2988899 C 329.88424,8.2988899 649.65644,-0.97095606 649.65644,267.85458 L 10.112034,267.85458 C 10.112034,-0.97095606 329.88424,8.2988899 329.88424,8.2988899 z" id="shoulder_outer" sodipodi:nodetypes="cccc"/>
    <text xml:space="preserve" style="font-size: 181.717px; font-style: normal; font-weight: normal; fill: rgb(0, 0, 0); fill-opacity: 1; stroke: none; stroke-width: 1px; stroke-linecap: butt; stroke-linejoin: miter; stroke-opacity: 1; font-family: Bitstream Vera Sans;" x="292.622" y="198.919" id="shoulder_button_text" transform="scale(0.929526, 1.07582)">
        <tspan sodipodi:role="line" id="tspan3704" x="292.622" y="198.919">%(button)s</tspan>
    </text>
  </g>

</svg>
"""

    readme = open('README.md', 'w')

    #for button in 'up down left right L R A B X Y START SELECT'.split():
    for button in 'L R A B X Y'.split():
        svg = str_template_round % {'button': button}
        print(svg)
        filename = button.lower() + '.svg'
        f = open(filename, 'w')
        f.write(svg)
        f.close()
        readme.write('![image](%s)\n\n' % filename)


    for button in 'L R'.split():
        svg = str_template_shoulder % {'button': button}
        print(svg)
        filename = button.lower() + '.svg'
        f = open(filename, 'w')
        f.write(svg)
        f.close()
        readme.write('![image](%s)\n\n' % filename)

    for button in 'START SELECT'.split():
        svg = str_template_start % {'button': button}
        print(svg)
        filename = button.lower() + '.svg'
        f = open(filename, 'w')
        f.write(svg)
        f.close()
        readme.write('![image](%s)\n\n' % filename)

    #for button in 'up down left right'.split():
    for button, highlight in [('up', 'matrix(0, 1, -1, 0, 600, 0)'), ('down', 'matrix(0, -1, 1, 0, 0, 600)'), ('left', ''), ('right', 'matrix(-1, 0, 0, -1, 600, 600)')]:
        svg = str_template_dpad % {'button': button, 'highlight': highlight}
        print(svg)
        filename = button.lower() + '.svg'
        f = open(filename, 'w')
        f.write(svg)
        f.close()
        readme.write('![image](%s)\n\n' % filename)

    readme.close()


def main(argv=None):
    if argv is None:
        argv = sys.argv

    print('Python %s on %s' % (sys.version, sys.platform))

    doit()

    return 0


if __name__ == "__main__":
    sys.exit(main())
