# -*- coding: utf-8 -*-

import os
    
walk_dir = 'C:/Users/kilicm/Desktop/images/'

for root, subdirs, files in os.walk(walk_dir):
    new_file_name = os.path.basename(root)+'.tex'
    list_file_path = os.path.join(root, new_file_name)
    print(list_file_path)
    with open(list_file_path, 'w') as list_file:
        images = []
        for filename in files:       
            images.append(filename)

        if len(images) >= 1:
            list_file.write(("""
\\documentclass{article}
\\usepackage[utf8]{inputenc}
\\usepackage{graphicx}
\\usepackage{subcaption}
\\setlength{\\voffset}{-0.75in}
\\setlength{\headsep}{5pt}
\n
\\begin{document} 

\\begin{figure} 
\\begin{center}
\\pagenumbering{gobble} 

\\huge \\textbf{Title} 
\\end{center} 
\\begin{tabular}{lp{11cm}} 

\\hfill  & \Large 	\\textbf{Name} \Large\hfill   	\\textbf{%s}
\\end{tabular} 
\\hspace*{-3cm} 
\\begin{subfigure}{0.5\\textwidth} 
\\centering 
\\includegraphics[scale=0.28]{%s} 
\\label{fig:sfig1} 
\\end{subfigure}%% 
\\hspace{1.5in} 
\\begin{subfigure}{0.5\\textwidth} 
\\centering 
\\includegraphics[scale=0.28]{%s} 
\\label{fig:sfig2} 
\\end{subfigure} 

\\hspace*{-3cm} 
\\begin{subfigure}{0.5\\textwidth} 
\\centering 
\\includegraphics[scale=0.28]{%s} 
\\label{fig:sfig1} 
\\end{subfigure}%% 
\\hspace{1.5in} 
\\begin{subfigure}{0.5\\textwidth} 
\\centering 
\\includegraphics[scale=0.28]{%s} 
\\label{fig:sfig2} 
\\end{subfigure} 

\\hspace*{-3cm} 
\\begin{subfigure}{.5\\textwidth} 
\\centering 
\\includegraphics[scale=0.28]{%s} 
\\label{fig:sfig1} 
\\end{subfigure}%% 
\\hspace{1.5in} 
\\begin{subfigure}{.5\\textwidth} 
\\centering 
\\includegraphics[scale=0.28]{%s} 
\\label{fig:sfig2} 
\\end{subfigure} 
 
\\end{figure}
\\end{document}""" % ( images[0].split('.png')[0].split('_')[-1], images[0], images[1],images[2], images[3],images[4], images[5])))

