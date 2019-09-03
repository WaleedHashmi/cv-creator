#!/usr/bin/env python
# -*- coding: utf8 -*-

import pandas as pd
import sys, getopt, os.path
import random

# Define variables
def read_data(data, row):
    print "Row:", row
    global nom 
    nom = data['nom'][row]
    global prenom 
    prenom = data['prenom'][row]
    global address
    address = data['candidat_adr'][row]
    global phone
    phone = data['candidat_tel'][row]
    global email
    email = data['candidat_mail'][row]
    global intitule_cv
    intitule_cv = data['intitule_cv'][row].encode('utf8')
    global intitule_exp
    intitule_exp = data['intitule_experiences'][row].encode('utf8')
    # 1er emploi
    global exp_title_1 
    exp_title_1 = data['exp1_title'][row].encode('utf8')
    global exp_date_start_month_1 
    exp_date_start_month_1 = data['exp1_date_start_month'][row]
    global exp_date_start_year_1 
    exp_date_start_year_1 = data['exp1_date_start_year'][row]
    # if(np.isnan(exp_date_start_year_1) | np.isnan(exp_date_start_year_1)): exp_date_start_year_1 = ""
    global exp_date_end_month_1 
    exp_date_end_month_1 = data['exp1_date_end_month'][row]
    # if(np.isnan(exp_date_end_month_1) | np.isnan(exp_date_end_month_1)): exp_date_end_month_1 = ""
    global exp_date_end_year_1 
    exp_date_end_year_1 = data['exp1_date_end_year'][row]
    # if(np.isnan(exp_date_end_year_1) | np.isnan(exp_date_end_year_1)): exp_date_end_year_1 = ""
    global exp_main_task_1_1 
    exp_main_task_1_1 = data['exp1_main_task1'][row].encode('utf8')
    global exp_main_task_1_2 
    exp_main_task_1_2 = data['exp1_main_task2'][row].encode('utf8')
    global exp_main_task_1_3 
    exp_main_task_1_3 = data['exp1_main_task3'][row].encode('utf8')
    global exp_employeur_1 
    exp_employeur_1 = data['exp1_employeur'][row].encode('utf8')
    global exp_adresse_1 
    exp_adresse_1 = data['exp1_adresse'][row].encode('utf8')
    # 2e emploi
    global exp_title_2 
    exp_title_2 = data['exp2_title'][row].encode('utf8')
    global exp_date_start_month_2 
    exp_date_start_month_2 = data['exp2_date_start_month'][row]
    global exp_date_start_year_2 
    exp_date_start_year_2 = data['exp2_date_start_year'][row]
    # if(np.isnan(exp_date_start_year_2) | np.isnan(exp_date_start_year_2)): exp_date_start_year_2 = ""
    global exp_date_end_month_2 
    exp_date_end_month_2 = data['exp2_date_end_month'][row]
    # if(np.isnan(exp_date_end_month_2) | np.isnan(exp_date_end_month_2)): exp_date_end_month_2 = ""
    global exp_date_end_year_2 
    exp_date_end_year_2 = data['exp2_date_end_year'][row]
    # if(np.isnan(exp_date_end_year_2) | np.isnan(exp_date_end_year_2)): exp_date_end_year_2 = ""
    global exp_main_task_2_1 
    exp_main_task_2_1 = data['exp2_main_task1'][row].encode('utf8')
    global exp_main_task_2_2 
    exp_main_task_2_2 = data['exp2_main_task2'][row].encode('utf8')
    global exp_main_task_2_3 
    exp_main_task_2_3 = data['exp2_main_task3'][row].encode('utf8')
    global exp_employeur_2 
    exp_employeur_2 = data['exp2_employeur'][row].encode('utf8')
    global exp_adresse_2 
    exp_adresse_2 = data['exp2_adresse'][row].encode('utf8')
    # 3e emploi
    global exp_title_3 
    exp_title_3 = data['exp3'][row].encode('utf8')
    global exp_date_start_month_3 
    exp_date_start_month_3 = data['exp3_date_start_month'][row].encode('utf8')
    global exp_date_start_year_3 
    exp_date_start_year_3 = data['exp3_date_start_year'][row]
    global exp_date_end_month_3 
    exp_date_end_month_3 = data['exp3_date_end_month'][row].encode('utf8')
    global exp_date_end_year_3 
    exp_date_end_year_3 = data['exp3_date_end_year'][row]
    global exp_main_task_3_1 
    exp_main_task_3_1 = data['exp3_main_task1'][row].encode('utf8')
    global exp_main_task_3_2 
    exp_main_task_3_2 = data['exp3_main_task2'][row].encode('utf8')
    global exp_main_task_3_3 
    exp_main_task_3_3 = data['exp3_main_task3'][row].encode('utf8')
    global exp_employeur_3 
    exp_employeur_3 = data['lieu_exp3'][row].encode('utf8')
    global exp_adresse_3 
    exp_adresse_3 = data['adr_exp3'][row].encode('utf8')
    # formations
    global intitule_formations 
    intitule_formations = data['intitule_formations'][row].encode('utf8')
    # 1ere formation
    global intitule_formation_1 
    intitule_formation_1 = data['formation1'][row].encode('utf8')
    global formation_lieu_1 
    formation_lieu_1 = data['formation1_lieu'][row].encode('utf8')
    global formation_adresse_1 
    formation_adresse_1 = data['formation1_adr'][row].encode('utf8')
    global formation_date_start_year_1 
    formation_date_start_year_1 = data['formation1_date_start_year'][row]
    global formation_date_end_year_1 
    formation_date_end_year_1 = data['formation1_end_start_year'][row]
    # 2e formation
    global intitule_formation_2 
    intitule_formation_2 = data['formation2'][row].encode('utf8')
    global formation_lieu_2 
    formation_lieu_2 = data['formation2_lieu'][row].encode('utf8')
    global formation_adresse_2 
    formation_adresse_2 = data['formation2_adr'][row].encode('utf8')
    global formation_date_start_year_2 
    formation_date_start_year_2 = data['formation2_date_start_year'][row]
    global formation_date_end_year_2 
    formation_date_end_year_2 = data['formation2_end_start_year'][row]
    # 3e formation
    global intitule_formation_3 
    intitule_formation_3 = data['formation3'][row].encode('utf8')
    global formation_lieu_3 
    formation_lieu_3 = data['formation3_lieu'][row].encode('utf8')
    global formation_adresse_3 
    formation_adresse_3 = data['formation3_adr'][row].encode('utf8')
    global formation_date_start_year_3 
    formation_date_start_year_3 = data['formation3_date_start_year'][row]
    global formation_date_end_year_3 
    formation_date_end_year_3 = data['formation3_end_start_year'][row]
    # Skills
    global intitule_skills 
    intitule_skills = data['intitule_skills'][row].encode('utf8')
    global skill1 
    skill1 = data['skill1'][row].encode('utf8')
    global skill2 
    skill2 = data['skill2'][row].encode('utf8')
    global skill3 
    skill3 = data['skill3'][row].encode('utf8')
    # Hobbies
    global intitule_hobbies 
    intitule_hobbies = data['intitule_hobbies'][row].encode('utf8')
    global hobbie1 
    hobbie1 = data['hobbie1'][row].encode('utf8')
    global hobbie2 
    hobbie2 = data['hobbie2'][row].encode('utf8')
    global hobbie3 
    hobbie3 = data['hobbie3'][row].encode('utf8')


# Define LaTeX file for ECV package and write it
def write_ecv(font):
    lines_start_1 = ['\documentclass[french]{ecv}\n',
                     '\\usepackage[T1]{fontenc}\n',
                     '\\usepackage[utf8]{inputenc}\n',
                     '\\usepackage[french]{babel}\n',
                     '\\usepackage{{{}}}\n'.format(font)]

    lines_start_2 = ['\\ecvName{{{} {}}}\n'.format(prenom, nom),
                     '\\begin{document}\n',
                     '\\begin{ecv}\n',
                     '\ecvSec{\hypertarget{hypertarget:\ecvPerson}{\ecvPerson}}\n',
                     '\ecvEPR{{Nom}}{{\\textsc{{{}}}, {}}}\n'.format(nom, prenom),
                     '\ecvEPR{{Adresse}}{{{}}}\n'.format(address),
                     '\ecvEPR{{T\\\'el.:}}{{{}}}\n'.format(phone),
                     '\ecvEPR{{M\\\'el:}}{{{}}}\n'.format(email),
                     '\ecvBSec{{{}}}\n'.format(intitule_exp),
                     '\ecvEFR{{P\\\'eriode}}{{{} - {}}}\n'.format(exp_date_start_year_1, exp_date_end_year_1),
                     '\ecvENR{{Employeur}}{{\ecvBold{{{}}}, {}}}\n'.format(exp_employeur_1, exp_adresse_1),
                     '\ecvENR{{Position}}{{{}}}\n'.format(exp_title_1),
                     '\ecvENR{{Responsabilit\\\'es}}{{{}, {}, {}}}\n'.format(exp_main_task_1_1, exp_main_task_1_2, exp_main_task_1_3)]

    lines_2e_emploi = ['\ecvEFR{{P\\\'eriode}}{{{} - {}}}\n'.format(exp_date_start_year_2, exp_date_end_year_2),
                     '\ecvENR{{Employeur}}{{\ecvBold{{{}}}, {}}}\n'.format(exp_employeur_2, exp_adresse_2),
                     '\ecvENR{{Position}}{{{}}}\n'.format(exp_title_2),
                     '\ecvENR{{Responsabilit\\\'es}}{{{}, {}, {}}}\n'.format(exp_main_task_2_1, exp_main_task_2_2, exp_main_task_2_3)]

    lines_3e_emploi = ['\ecvEFR{{P\\\'eriode}}{{{} - {}}}\n'.format(exp_date_start_year_3, exp_date_end_year_3),
                     '\ecvENR{{Employeur}}{{\ecvBold{{{}}}, {}}}\n'.format(exp_employeur_3, exp_adresse_3),
                     '\ecvENR{{Position}}{{{}}}\n'.format(exp_title_3),
                     '\ecvENR{{Responsabilit\\\'es}}{{{}, {}, {}}}\n'.format(exp_main_task_3_1, exp_main_task_3_2, exp_main_task_3_3)]

    lines_formation = ['\ecvBSec{{{}}}\n'.format(intitule_formations),
                       '\ecvEFR{{P\\\'eriode}}{{{} - {}}}\n'.format(formation_date_start_year_1, formation_date_end_year_1),
                       '\ecvENR{{Dipl\^ome}}{{\ecvBold{{{}}}}}\n'.format(intitule_formation_1),
                       '\ecvENR{{\\\'Etablissement}}{{{}, {}}}\n'.format(formation_lieu_1, formation_adresse_1)]


    lines_2e_formation = ['\ecvEFR{{P\\\'eriode}}{{{} - {}}}\n'.format(formation_date_start_year_2, formation_date_end_year_2),
                       '\ecvENR{{Dipl\^ome}}{{\ecvBold{{{}}}}}\n'.format(intitule_formation_2),
                       '\ecvENR{{\\\'Etablissement}}{{{}, {}}}\n'.format(formation_lieu_2, formation_adresse_2)]

    lines_3e_formation = ['\ecvEFR{{P\\\'eriode}}{{{} - {}}}\n'.format(formation_date_start_year_3, formation_date_end_year_3),
                       '\ecvENR{{Dipl\^ome}}{{\ecvBold{{{}}}}}\n'.format(intitule_formation_3),
                       '\ecvENR{{\\\'Etablissement}}{{{}, {}}}\n'.format(formation_lieu_3, formation_adresse_3)]

    lines_skills_hobbies = ['\ecvBSec{{{}}}\n'.format(intitule_hobbies),
                            '\ecvEBSub{{}}{{{}, {}, {}}}\n'.format(hobbie1, hobbie2, hobbie3)]

    with open('{}/{}_ecv_{}.tex'.format(outputdir, intitule_cv, font), 'w') as f:
        f.writelines(lines_start_1)
        if font == 'tgheros' or font == 'tgadventor':
            f.writelines('\\renewcommand{\\familydefault}{\sfdefault}\n')
        f.writelines(lines_start_2)
        if exp_title_2 == '':
            pass
        else:
            f.writelines(lines_2e_emploi)
        if exp_title_3 == '':
            pass
        else:
            f.writelines(lines_3e_emploi)
        f.writelines(lines_formation)
        if intitule_formation_2 == '':
            pass
        else:
            f.writelines(lines_2e_formation)
        if intitule_formation_3 == '':
            pass
        else:
            f.writelines(lines_3e_formation)
        f.writelines(lines_skills_hobbies)
        f.write('\end{ecv}\n')
        f.write('\end{document}')


# Define LaTeX file for moderncv package and write it
def write_moderncv(layout, font):
    color = "black"
    scale = "0.8"
    lines_start_1 = ["\documentclass[12pt,a4paper]{moderncv}\n",
                     "\\usepackage[T1]{fontenc}\n",
                     "\\usepackage[utf8]{inputenc}\n",
                     "\\usepackage[french]{babel}\n",
                     "\\usepackage[scale={}]{{geometry}}\n".format(scale),
                     "\moderncvstyle{{{}}}\n".format(layout),
                     "\moderncvcolor{{{}}}\n".format(color),
                     "\\usepackage{{{}}}\n".format(font)]

    lines_start_2 = ["\\name{{{}}}{{{}}}\n".format(prenom, nom),
                     "\\address{{{}}}\n".format(address),
                     "\phone{{{}}}\n".format(phone),
                     "\email{{{}}}\n".format(email),
                     "\\begin{document}\n",
                     "\setcounter{secnumdepth}{0}\n",
                     "\makecvtitle\n",
                     "\section{{{}}}\n".format(intitule_exp),
                     "\cventry{{{} {} - {} {}}}{{{}}}{{{}}}{{{}}}{{}}{{{}\\newline{{}}{}\\newline{{}}{}}}\n".format(
                         exp_date_start_month_1,
                         int(exp_date_start_year_1),
                         exp_date_end_month_1,
                         exp_date_end_year_1,
                         exp_title_1,
                         exp_employeur_1,
                         exp_adresse_1,
                         exp_main_task_1_1,
                         exp_main_task_1_2,
                         exp_main_task_1_3)]

    lines_2e_emploi = [
        "\cventry{{{} {} - {} {}}}{{{}}}{{{}}}{{{}}}{{}}{{{}\\newline{{}}{}\\newline{{}}{}}}\n".format(
            exp_date_start_month_2,
            int(exp_date_start_year_2),
            exp_date_end_month_2,
            int(exp_date_end_year_2),
            exp_title_2,
            exp_employeur_2,
            exp_adresse_2,
            exp_main_task_2_1,
            exp_main_task_2_2,
            exp_main_task_2_3)]

    lines_3e_emploi = [
        "\cventry{{{} {} - {} {}}}{{{}}}{{{}}}{{{}}}{{}}{{{}\\newline{{}}{}\\newline{{}}{}}}\n".format(
            exp_date_start_month_3,
            exp_date_start_year_3,
            exp_date_end_month_3,
            exp_date_end_year_3,
            exp_title_3,
            exp_employeur_3,
            exp_adresse_3,
            exp_main_task_3_1,
            exp_main_task_3_2,
            exp_main_task_3_3)]

    lines_1ere_formation = ["\section{{{}}}\n".format(intitule_formations),
                       "\cventry{{{} - {}}}{{{}}}{{{}}}{{{}}}{{}}{{}}\n".format(
                           formation_date_start_year_1,
                           formation_date_end_year_1,
                           intitule_formation_1,
                           formation_lieu_1,
                           formation_adresse_1)]

    lines_2e_formation = ["\cventry{{{} - {}}}{{{}}}{{{}}}{{{}}}{{}}{{}}\n".format(
        formation_date_start_year_2,
        formation_date_end_year_2,
        intitule_formation_2,
        formation_lieu_2,
        formation_adresse_2)]

    lines_3e_formation = ["\cventry{{{} - {}}}{{{}}}{{{}}}{{{}}}{{}}{{}}\n".format(
        formation_date_start_year_3,
        formation_date_end_year_3,
        intitule_formation_3,
        formation_lieu_3,
        formation_adresse_3)]

    lines_skills_hobbies = ["\section{{{}}}\n".format(intitule_skills),
                            "\cvlistitem{{{}}}\n".format(skill1),
                            "\cvlistitem{{{}}}\n".format(skill2),
                            "\cvlistitem{{{}}}\n".format(skill3),
                            "\section{{{}}}\n".format(intitule_hobbies),
                            "\cvlistitem{{{}}}\n".format(hobbie1),
                            "\cvlistitem{{{}}}\n".format(hobbie2),
                            "\cvlistitem{{{}}}\n".format(hobbie3)]

    with open('./{}/{}_{}_{}.tex'.format(outputdir, intitule_cv, layout, font),
              "w") as f:
        f.writelines(lines_start_1)
        if font == 'tgheros' or font == 'tgadventor':
            f.writelines('\\renewcommand{\\familydefault}{\sfdefault}\n')
        f.writelines(lines_start_2)
        if exp_title_2 == '':
            pass
        else:
            f.writelines(lines_2e_emploi)
        if exp_title_3 == '':
            pass
        else:
            f.writelines(lines_3e_emploi)
        f.writelines(lines_1ere_formation)
        if intitule_formation_2 == '':
            pass
        else:
            f.writelines(lines_2e_formation)
        if intitule_formation_3 == '':
            pass
        else:
            f.writelines(lines_3e_formation)
        f.writelines(lines_skills_hobbies)
        f.write("\end{document}")


# Define LaTeX file for cleancv package and write it
def write_cleancv():
    lines_start_1 = ["\documentclass[a4paper,11pt]{article}\n",
                    "\usepackage[T1]{fontenc}\n",
                    "\usepackage[utf8]{inputenc}\n",
                    #"\usepackage{lmodern}\n",
                    #"\\renewcommand{\\familydefault}{\sfdefault}\n",
                    "\\newlength{\outerbordwidth}\n",
                    "\pagestyle{empty}\n",
                    "\\raggedbottom\n",
                    "\usepackage[svgnames]{xcolor}\n",
                    "\usepackage{framed}\n",
                    "\usepackage{tocloft}\n"
                    "\setlength{\outerbordwidth}{3pt}\n",
                    "\definecolor{shadecolor}{gray}{0.75}\n",
                    "\definecolor{shadecolorB}{gray}{0.93}\n",
                    "\setlength{\evensidemargin}{-0.25in}\n",
                    "\setlength{\headheight}{0in}\n",
                    "\setlength{\headsep}{0in}\n", 
                    "\setlength{\oddsidemargin}{-0.25in}\n",
                    "\setlength{\paperheight}{11in}\n",
                    "\setlength{\paperwidth}{8.5in}\n",
                    "\setlength{\\tabcolsep}{0in}\n",
                    "\setlength{\\textheight}{9.5in}\n",
                    "\setlength{\\textwidth}{7in}\n",
                    "\setlength{\\topmargin}{-0.3in}\n",
                    "\setlength{\\topskip}{0in}\n",
                    "\setlength{\\voffset}{0.1in}\n",
                    "\\newcommand{\\resitem}[1]{\item #1 \\vspace{-2pt}}\n",
                    "\\newcommand{\\resheading}[1]{\\vspace{8pt}\n",
                    "\parbox{\\textwidth}{\setlength{\FrameSep}{\outerbordwidth}\n",
                    "\\begin{shaded}\n",
                    "\setlength{\\fboxsep}{0pt}\\framebox[\\textwidth][l]{\setlength{\\fboxsep}{4pt}\\fcolorbox{shadecolorB}{shadecolorB}{\\textbf{\sffamily{\mbox{~}\makebox[6.762in][l]{\large #1} \\vphantom{p\^{E}}}}}}\n",
                    "\end{shaded}\n",
                    "}\\vspace{-5pt}\n",
                    "}\n",
                    "\\newcommand{\\ressubheading}[4]{\n",
                    "\\begin{tabular*}{6.5in}{l@{\extracolsep{\\fill}}r}\n",
                    "\\textbf{#1} & #2 \\\\\n",
                    "\\textit{#3} & \\textit{#4} \\\\\n",
                    "\end{tabular*}\\vspace{-6pt}}\n",
                    "\\begin{document}\n", 
                    "\\begin{tabular*}{7in}{l@{\extracolsep{\\fill}}r}\n",
                    "\\textbf{{\Large {} {}}} & \\textbf{{\\today}}\\\\\n".format(prenom, nom),
                    "& {} \\\\\n".format(email),
                    "{} & {}\\\\\n".format(address, phone),
                    "\end{tabular*}\n"]
    lines_1er_emploi = ["\\resheading{{{}}}\n".format(intitule_exp),
                        "\\begin{itemize}\n",
                        "\item \\ressubheading{{{}}}{{{} {} - {} {}}}{{{}}}{{{}}}\n".format(exp_title_1, exp_date_start_month_1, exp_date_start_year_1, exp_date_end_month_1, exp_date_end_year_1, exp_employeur_1, exp_adresse_1),
                        "\\begin{itemize}\n",
                        "\\resitem{{{}}}\n".format(exp_main_task_1_1),
                        "\\resitem{{{}}}\n".format(exp_main_task_1_2),
                        "\\resitem{{{}}}\n".format(exp_main_task_1_3),
                        "\end{itemize}\n"]
    lines_2e_emploi = [ "\item \\ressubheading{{{}}}{{{} {} - {} {}}}{{{}}}{{{}}}\n".format(exp_title_2, exp_date_start_month_2, exp_date_start_year_2, exp_date_end_month_2, exp_date_end_year_2, exp_employeur_2, exp_adresse_2),
                        "\\begin{itemize}\n",
                        "\\resitem{{{}}}\n".format(exp_main_task_2_1),
                        "\\resitem{{{}}}\n".format(exp_main_task_2_2),
                        "\\resitem{{{}}}\n".format(exp_main_task_2_3),
                        "\end{itemize}\n"]
    lines_3e_emploi = [ "\item \\ressubheading{{{}}}{{{} {} - {} {}}}{{{}}}{{{}}}\n".format(exp_title_3, exp_date_start_month_3, exp_date_start_year_3, exp_date_end_month_3, exp_date_end_year_3, exp_employeur_3, exp_adresse_3),
                        "\\begin{itemize}\n",
                        "\\resitem{{{}}}\n".format(exp_main_task_3_1),
                        "\\resitem{{{}}}\n".format(exp_main_task_3_2),
                        "\\resitem{{{}}}\n".format(exp_main_task_3_3),
                        "\end{itemize}\n"]
    lines_1ere_formation = ["\\resheading{{{}}}\n".format(intitule_formations),
                            "\\begin{itemize}\n",
                            "\item \\ressubheading{{{}}}{{{} - {}}}{{{}}}{{{}}}\n".format(intitule_formation_1, formation_date_start_year_1, formation_date_end_year_1, formation_lieu_1, formation_adresse_1)]
    lines_2e_formation = ["\item \\ressubheading{{{}}}{{{} - {}}}{{{}}}{{{}}}\n".format(intitule_formation_2, formation_date_start_year_2, formation_date_end_year_2, formation_lieu_2, formation_adresse_2)]
    lines_3e_formation = ["\item \\ressubheading{{{}}}{{{} - {}}}{{{}}}{{{}}}\n".format(intitule_formation_3, formation_date_start_year_3, formation_date_end_year_3, formation_lieu_3, formation_adresse_3)]
    lines_skills_hobbies = ["\\resheading{{{}}}\n".format(intitule_skills),
                            "\\begin{itemize}\n",
                            "\\resitem{{{}}}\n".format(skill1),
                            "\\resitem{{{}}}\n".format(skill2),
                            "\\resitem{{{}}}\n".format(skill3),
                            "\end{itemize}\n",
                            "\\resheading{{{}}}\n".format(intitule_hobbies),
                            "\\begin{itemize}\n",
                            "\\resitem{{{}}}\n".format(hobbie1),
                            "\\resitem{{{}}}\n".format(hobbie2),
                            "\\resitem{{{}}}\n".format(hobbie3),
                            "\end{itemize}\n"]
    with open('./{}/{}_cleancv.tex'.format(outputdir, intitule_cv), "w") as f:
        f.writelines(lines_start_1)
        if font == 'tgheros' or font == 'tgadventor':
            f.writelines('\\renewcommand{\\familydefault}{\sfdefault}\n')
        f.writelines(lines_1er_emploi)
        if exp_title_2 == '':
            pass
        else:
            f.writelines(lines_2e_emploi)
        if exp_title_3 == '':
            pass
        else:
            f.writelines(lines_3e_emploi)
        f.writelines("\end{itemize}\n")
        f.writelines(lines_1ere_formation)
        if intitule_formation_2 == '':
            pass
        else:
            f.writelines(lines_2e_formation)
        if intitule_formation_3 == '':
            pass
        else:
            f.writelines(lines_3e_formation)
        f.writelines("\end{itemize}\n")
        f.writelines(lines_skills_hobbies)
        f.write("\end{document}")


# Define LaTeX file for CVUS package and write it
def write_cvus():
    lines_start_1 = ["\documentclass[letterpaper]{article}\n",
                    "\usepackage{hyperref}\n",
                    "\usepackage{geometry}\n",
                    "\usepackage[T1]{fontenc}\n",
                    "\usepackage[utf8]{inputenc}\n",
                    #"\usepackage[sc,osf]{mathpazo}\n",
                    "\usepackage[sfdefault,book]{FiraSans}\n",
                    "\\renewcommand{\\familydefault}{\sfdefault}\n",
                    "\def\\name{{{} {}}}\n".format(prenom, nom),
                    "\def\\footerlink{}\n",
                    "\hypersetup{colorlinks = true,urlcolor = black,pdfauthor = {\\name}, pdftitle = {\\name: Curriculum Vitae}, pdfsubject = {Curriculum Vitae}, pdfpagemode = UseNone}\n",
                    "\geometry{body={6.5in, 8.5in}, left=1.0in, top=1.25in}\n",
                    "\pagestyle{myheadings}\n",
                    "\markright{\\name}\n",
                    "\\thispagestyle{empty}\n",
                    "\usepackage{sectsty}\n",
                    "\sectionfont{\\rmfamily\mdseries\Large}\n",
                    "\subsectionfont{\\rmfamily\mdseries\itshape\large}\n",
                    "\setlength\parindent{0em}\n",
                    "\\renewenvironment{itemize}{\\begin{list}{}{\setlength{\leftmargin}{1.5em}}}{\end{list}}\n",
                    "\\begin{document}\n",
                    "{\huge \\name}\n\n",
                    "\\vspace{0.25in}\n\n",
                    "\\begin{minipage}{0.8\linewidth}\n",
                    "{}\n".format(address),
                    "\end{minipage}\n",
                    "\\begin{minipage}{0.2\linewidth}\n",
                    "\\begin{tabular}{ll}\n",
                    "T\\'el.: & {}\\\\\n".format(phone),
                    "Email: & {}\\\\\n".format(email),
                    "\end{tabular}\n",
                    "\end{minipage}\n",
                    "\section*{{{}}}\n".format(intitule_exp),
                    "\\begin{itemize}\n",
                    "\item \\textbf{{{}}}\hfill {} {} - {} {}\\\\{}\hfill {}\n\n".format(exp_title_1, exp_date_start_month_1, exp_date_start_year_1, exp_date_end_month_1, exp_date_end_year_1, exp_employeur_1, exp_adresse_1),
                    "\\begin{itemize}\n",
                    "\item- {}\n".format(exp_main_task_1_1),
                    "\item- {}\n".format(exp_main_task_1_2),
                    "\item- {}\n".format(exp_main_task_1_3),
                    "\\end{itemize}\n"]
    lines_2e_emploi = ["\item \\textbf{{{}}}\hfill {} {} - {} {}\\\\{}\hfill {}\n\n".format(exp_title_2, exp_date_start_month_2, exp_date_start_year_2, exp_date_end_month_2, exp_date_end_year_2, exp_employeur_2, exp_adresse_2),
                    "\\begin{itemize}\n",
                    "\item- {}\n".format(exp_main_task_2_1),
                    "\item- {}\n".format(exp_main_task_2_2),
                    "\item- {}\n".format(exp_main_task_2_3),
                    "\\end{itemize}\n"]
    lines_3e_emploi = ["\item \\textbf{{{}}}\hfill {} {} - {} {}\\\\{}\hfill {}\n\n".format(exp_title_3, exp_date_start_month_3, exp_date_start_year_3, exp_date_end_month_3, exp_date_end_year_3, exp_employeur_3, exp_adresse_3),
                    "\\begin{itemize}\n",
                    "\item- {}\n".format(exp_main_task_3_1),
                    "\item- {}\n".format(exp_main_task_3_2),
                    "\item- {}\n".format(exp_main_task_3_3),
                    "\\end{itemize}\n"]
    lines_formation = ["\section*{{{}}}\n".format(intitule_formations),
                        "\\begin{itemize}\n",
                        "\item \\textbf{{{}}} \hfill {} - {}\\\\{} \hfill {}\n".format(intitule_formation_1, formation_date_start_year_1, formation_date_end_year_1, formation_lieu_1, formation_adresse_1)]
    lines_2e_formation = ["\item \\textbf{{{}}} \hfill {} - {}\\\\{} \hfill {}\n".format(intitule_formation_2, formation_date_start_year_2, formation_date_end_year_2, formation_lieu_2, formation_adresse_2)]
    lines_3e_formation = ["\item \\textbf{{{}}} \hfill {} - {}\\\\{} \hfill {}\n".format(intitule_formation_3, formation_date_start_year_3, formation_date_end_year_3, formation_lieu_3, formation_adresse_3)]
    lines_skills_hobbies = ["\section*{{{}}}\n".format(intitule_skills),
                            "\\begin{itemize}\n",
                            "\item {}\n".format(skill1),
                            "\item {}\n".format(skill2),
                            "\item {}\n".format(skill3),
                            "\end{itemize}\n",
                            "\section*{{{}}}\n".format(intitule_hobbies),
                            "\\begin{itemize}\n",
                            "\item {}\n".format(hobbie1),
                            "\item {}\n".format(hobbie2),
                            "\item {}\n".format(hobbie3),
                            "\end{itemize}\n"]
    with open('./{}/{}_cvus.tex'.format(outputdir, intitule_cv), "w") as f:
        f.writelines(lines_start_1)
        #if font == 'tgheros' or font == 'tgadventor':
        #    f.writelines('\\renewcommand{\\familydefault}{\sfdefault}\n')
        if exp_title_2 == '':
            pass
        else:
            f.writelines(lines_2e_emploi)
        if exp_title_3 == '':
            pass
        else:
            f.writelines(lines_3e_emploi)
        f.writelines("\\end{itemize}\n")
        f.writelines(lines_formation)
        if intitule_formation_2 == '':
            pass
        else:
            f.writelines(lines_2e_formation)
        if intitule_formation_3 == '':
            pass
        else:
            f.writelines(lines_3e_formation)
        f.writelines("\\end{itemize}\n")
        f.writelines(lines_skills_hobbies)
        f.write("\end{document}")


# Define LaTeX file for simplecv package and write it
def write_simple():
    lines_start_1 = ["\documentclass[a4paper,MMMyyyy]{simpleresumecv}\n",
                    "\\usepackage[T1]{fontenc}\n",
                    "\\usepackage[utf8]{inputenc}\n",
                    "\\usepackage[french]{babel}\n",
                    "\\newcommand{{\CVAuthor}}{{{} {}}}\n".format(prenom, nom),
                    "\\newcommand{\CVTitle}{}\n",
                    "\\newcommand{\CVNote}{}\n",
                    "\\newcommand{\CVWebpage}{}\n",
                    "\hypersetup{\n",
                    "pdftitle={\CVTitle},\n",
                    "pdfauthor={\CVAuthor},\n",
                    "pdfsubject={\CVWebpage},\n",
                    "pdfcreator={XeLaTeX},\n",
                    "pdfproducer={},\n",
                    "pdfkeywords={},\n",
                    "unicode=true,\n",
                    "bookmarks=true,\n",
                    "bookmarksopen=true,\n",
                    "pdfstartview=FitH,\n",
                    "pdfpagelayout=OneColumn,\n",
                    "pdfpagemode=UseOutlines,\n",
                    "hidelinks,\n",
                    "breaklinks}\n",
                    "\\newcommand{\Code}[1]{\mbox{\\textbf{#1}}}\n",
                    "\\newcommand{\CodeCommand}[1]{\mbox{\\textbf{\\textbackslash{#1}}}}\n",
                    "\\begin{document}\n",
                    "\Title{\CVAuthor}\n",
                    "\\begin{SubTitle}\n",
                    "{}\n".format(address),
                    "\par\n {}\n".format(email),
                    "\,\SubBulletSymbol\,\n {}\n".format(phone),
                    "\end{SubTitle}\n",
                    "\\begin{Body}\n"]
    lines_start_2 = ["\Section{{{}}}{{{}}}{{}}\n".format(intitule_exp, intitule_exp),
                        "\Entry\\textbf{{{}}}".format(exp_title_1),
                        "\hfill\DatestampYM{{{}}}{{{}}} - \DatestampYM{{{}}}{{{}}}\n".format(exp_date_start_year_1, exp_date_start_month_1, exp_date_end_year_1, exp_date_end_month_1),
                        "\Gap\n",
                        "{}, {}\n".format(exp_employeur_1, exp_adresse_1)]
    lines_2e_emploi = [ "\Entry\\textbf{{{}}}".format(exp_title_2),
                        "\hfill\DatestampYM{{{}}}{{{}}} - \DatestampYM{{{}}}{{{}}}\n".format(exp_date_start_year_2, exp_date_start_month_2, exp_date_end_year_2, exp_date_end_month_2),
                        "\Gap\n",
                        "{}, {}\n".format(exp_employeur_2, exp_adresse_2)]
    lines_3e_emploi = [ "\Entry\\textbf{{{}}}".format(exp_title_3),
                        "\hfill\DatestampYM{{{}}}{{{}}} - \DatestampYM{{{}}}{{{}}}\n".format(exp_date_start_year_3, exp_date_start_month_3, exp_date_end_year_3, exp_date_end_month_3),
                        "\Gap\n",
                        "{}, {}\n".format(exp_employeur_3, exp_adresse_3)]
    lines_formation = ["\Section{{{}}}{{{}}}{{}}\n".format(intitule_formations, intitule_formations),
                        "\Entry\\textbf{{{}}}".format(intitule_formation_1),
                        "\hfill\DatestampY{{{}}} - \DatestampY{{{}}}\n".format(formation_date_start_year_1, formation_date_end_year_1),
                        "\Gap\n",
                        "{}, {}\n".format(formation_lieu_1, formation_adresse_1)]
    lines_2e_formation = ["\Entry\\textbf{{{}}}".format(intitule_formation_2),
                        "\hfill\DatestampY{{{}}} - \DatestampY{{{}}}\n".format(formation_date_start_year_2, formation_date_end_year_2),
                        "\Gap\n",
                        "{}, {}\n".format(formation_lieu_1, formation_adresse_2)]
    lines_3e_formation = ["\Entry\\textbf{{{}}}".format(intitule_formation_3),
                        "\hfill\DatestampY{{{}}} - \DatestampY{{{}}}\n".format(formation_date_start_year_3, formation_date_end_year_3),
                        "\Gap\n",
                        "{}, {}\n".format(formation_lieu_1, formation_adresse_3)]
    lines_skills_hobbies = ["\Section{{{}}}{{{}}}{{}}\n".format(intitule_skills, intitule_skills),
                            "\Gap\n",
                            "\BulletItem\n",
                            "{}\n".format(skill1),
                            "\BulletItem\n",
                            "{}\n".format(skill2),
                            "\BulletItem\n",
                            "{}\n".format(skill3),
                            "\BigGap\n",
                            "\Section{{{}}}{{{}}}{{}}\n".format(intitule_hobbies, intitule_hobbies),
                            "\Gap\n",
                            "\BulletItem\n",
                            "{}\n".format(hobbie1),
                            "\BulletItem\n",
                            "{}\n".format(hobbie2),
                            "\BulletItem\n",
                            "{}\n".format(hobbie3)]
    with open('./{}/{}_simplecv.tex'.format(outputdir, intitule_cv), "w") as f:
        f.writelines(lines_start_1)
        if font == 'tgheros' or font == 'tgadventor':
            f.writelines('\\renewcommand{\\familydefault}{\sfdefault}\n')
        f.writelines(lines_start_2)
        if exp_title_2 == '':
            pass
        else:
            f.writelines("\BigGap\n")
            f.writelines(lines_2e_emploi)
        if exp_title_3 == '':
            pass
        else:
            f.writelines("\BigGap\n")
            f.writelines(lines_3e_emploi)
        f.writelines(lines_formation)
        if intitule_formation_2 == '':
            pass
        else:
            f.writelines("\BigGap\n")
            f.writelines(lines_2e_formation)
        if intitule_formation_3 == '':
            pass
        else:
            f.writelines("\BigGap\n")
            f.writelines(lines_3e_formation)
        f.writelines(lines_skills_hobbies)
        f.write("\end{Body}\n")
        f.write("\end{document}")

def write_academic(font):
    lines_start_1 = ["\documentclass[letterpaper,11pt,oneside]{article}\n",
                    "\usepackage[utf8]{inputenc}\n",
                    "\usepackage{setspace}\n",
                    "\usepackage{hyperref}\n",
                    "\usepackage[left=1in, right=1in, bottom=1.25in, top=1.25in]{geometry}\n",
                    "\pagenumbering{gobble}\n",
                    "\usepackage{{{}}}\n".format(font)]
    lines_start_2 = ["\\begin{document}\n",
                    "\\noindent  \LARGE{{\\textbf{{{} {}}}}}  \\\\ \n".format(prenom, nom),
                    "\\vspace{-2ex}\n",
                    "\hrule \n",
                    "\\normalsize\n",
                    "\\begin{center}\n",
                    "\\begin{tabular}{l l}\n",
                    "{} & \hspace{{1in}} {} \\\\ \n".format(address, email),
                    "& \hspace{{1in}} T\\'el.:  \\\\ \n".format(phone),
                    "\end{tabular}\n",
                    "\end{center}\n",
                    "\\noindent \\begin{tabular}{@{} l l}\n",
                    "\Large{{{}}}    &  \\\\\n".format(intitule_exp)]
    lines_1er_emploi = ["{} {} - {} {}&\\textbf{{{}}}\\\\\n".format(exp_date_start_month_1, exp_date_start_year_1, exp_date_end_month_1, exp_date_end_year_1, exp_title_1),
                        "&{}\\\\\n".format(exp_employeur_1),
                        "&{}\\\\\n".format(exp_adresse_1),
                        "&\\\\\n",
                        "&{}, {}, {}\\\\\n".format(exp_main_task_1_1, exp_main_task_1_2, exp_main_task_1_3)]
    lines_2e_emploi = ["{} {} - {} {}&\\textbf{{{}}}\\\\\n".format(exp_date_start_month_2, exp_date_start_year_2, exp_date_end_month_2, exp_date_end_year_2, exp_title_2),
                        "&{}\\\\\n".format(exp_employeur_2),
                        "&{}\\\\\n".format(exp_adresse_2),
                        "&\\\\\n",
                        "&{}, {}, {}\\\\\n".format(exp_main_task_2_1, exp_main_task_2_2, exp_main_task_2_3)]
    lines_3e_emploi = ["{} {} - {} {}&\\textbf{{{}}}\\\\\n".format(exp_date_start_month_3, exp_date_start_year_3, exp_date_end_month_3, exp_date_end_year_3, exp_title_3),
                        "&{}\\\\\n".format(exp_employeur_3),
                        "&{}\\\\\n".format(exp_adresse_3),
                        "&\\\\\n",
                        "&{}, {}, {}\\\\\n".format(exp_main_task_3_1, exp_main_task_3_2, exp_main_task_3_3)]
    lines_1ere_formation = ["\\Large{{{}}}&\\\\\n".format(intitule_formations),
                            "&\\\\\n",
                            "{} - {}&\\textbf{{{}}}\\\\\n".format(formation_date_start_year_1, formation_date_end_year_1, intitule_formation_1),
                            "&{}\\\\\n".format(formation_lieu_1),
                            "&{}\\\\\n".format(formation_adresse_1)]
    lines_2e_formation = ["{} - {}&\\textbf{{{}}}\\\\\n".format(formation_date_start_year_2, formation_date_end_year_2, intitule_formation_2),
                            "&{}\\\\\n".format(formation_lieu_2),
                            "&{}\\\\\n".format(formation_adresse_2)]
    lines_3e_formation = ["{} - {}&\\textbf{{{}}}\\\\\n".format(formation_date_start_year_3, formation_date_end_year_3, intitule_formation_3),
                            "&{}\\\\\n".format(formation_lieu_3),
                            "&{}\\\\\n".format(formation_adresse_3)]
    lines_skills_hobbies = ["\\Large{{{}}}&\\\\\n".format(intitule_skills),
                            "&{}\\\\\n".format(skill1),
                            "&{}\\\\\n".format(skill2),
                            "&{}\\\\\n".format(skill3),
                            "&\\\\\n",
                            "\\Large{{{}}}&\\\\\n".format(intitule_hobbies),
                            "&{}\\\\\n".format(hobbie1),
                            "&{}\\\\\n".format(hobbie2),
                            "&{}\\\\\n".format(hobbie3)]
    with open('./{}/{}_academic.tex'.format(outputdir, intitule_cv), "w") as f:
        f.writelines(lines_start_1)
        if font == 'tgheros' or font == 'tgadventor' or font == "kpfonts":
            f.writelines('\\renewcommand{\\familydefault}{\sfdefault}\n')
        f.writelines(lines_start_2)
        f.writelines("&\\\\\n")
        f.writelines(lines_1er_emploi)
        if not exp_title_2:
            pass
        else:
            f.writelines("&\\\\\n")
            f.writelines(lines_2e_emploi)
        if not exp_title_3:
            pass
        else:
            f.writelines("&\\\\\n")
            f.writelines(lines_3e_emploi)
        f.writelines("&\\\\\n")
        f.writelines(lines_1ere_formation)
        if not intitule_formation_2:
            pass
        else:
            f.writelines("&\\\\\n")
            f.writelines(lines_2e_formation)
        if not intitule_formation_3:
            pass
        else:
            f.writelines("&\\\\\n")
            f.writelines(lines_3e_formation)
        f.writelines("&\\\\\n")
        f.writelines(lines_skills_hobbies)
        f.write("\end{tabular}\n")
        f.write("\end{document}")

def write_professional(font):
    lines_start_1 = ["\documentclass[a4paper,10pt]{article}\n",
                    "\usepackage{marvosym}\n",
                    "\usepackage[T1]{fontenc}\n",
                    "\usepackage[utf8]{inputenc}\n",
                    "\usepackage[french]{babel}\n",
                    "\usepackage{fullpage}\n",
                    "\usepackage{{{}}}\n".format(font),
                    "\RequirePackage{color,graphicx}\n",
                    "\usepackage[usenames,dvipsnames]{xcolor}\n",
                    "\usepackage{titlesec}\n",
                    "\usepackage{hyperref}\n",
                    "\definecolor{linkcolour}{rgb}{0,0.2,0.6}\n",
                    "\hypersetup{colorlinks,breaklinks,urlcolor=linkcolour, linkcolor=linkcolour}\n",
                    "\\titleformat{\section}{\Large\scshape\\raggedright}{}{0em}{}[\\titlerule]\n",
                    "\\titlespacing{\section}{0pt}{3pt}{3pt}\n",
                    "\\begin{document}\n",
                    "\pagestyle{empty}\n",
                    "\par{{\centering{{\Huge {} \\textsc{{{}}}\\bigskip\par}}}}\n".format(prenom, nom),
                    "\section{Coordonn\\'ees}\n",
                    "\\begin{tabular}{rl}\n",
                    "\\textsc{{Adresse:}}&{}\\\\\n".format(address),
                    "\\textsc{{T\\'el:}} &{}\\\\\n".format(phone),
                    "\\textsc{{Email:}}  & {}\\\\\n".format(email),
                    "\end{tabular}\n"]
    lines_start_2 = []
    lines_1er_emploi = ["\section{{{}}}\n".format(intitule_exp),
                        "\\begin{tabular}{r|p{11cm}}\n",
                        "\\textsc{{{} {} - {} {}}}&{}\\\\\n".format(exp_date_start_month_1, exp_date_start_year_1, exp_date_end_month_1, exp_date_end_year_1, exp_title_1),
                        "&\\textsc{{{}}}\\\\\n".format(exp_employeur_1),
                        "&\small{{{}}}\\\\\n".format(exp_adresse_1),
                        "&\\\\\n",
                        "&{}, {}, {}\\\\\n".format(exp_main_task_1_1, exp_main_task_1_2, exp_main_task_1_3)]
                        #"\multicolumn{2}{c}{}\\\\\n"]
    lines_2e_emploi = ["\\textsc{{{} {} - {} {}}}&{}\\\\\n".format(exp_date_start_month_2, exp_date_start_year_2, exp_date_end_month_2, exp_date_end_year_2, exp_title_2),
                        "&\\textsc{{{}}}\\\\\n".format(exp_employeur_2),
                        "&\small{{{}}}\\\\\n".format(exp_adresse_2),
                        "&\\\\\n",
                        "&{}, {}, {}\\\\\n".format(exp_main_task_2_1, exp_main_task_2_2, exp_main_task_2_3)]
                        #"\multicolumn{2}{c}{}\\\\\n"]
    lines_3e_emploi = ["\\textsc{{{} {} - {} {}}}&{}\\\\\n".format(exp_date_start_month_3, exp_date_start_year_3, exp_date_end_month_3, exp_date_end_year_3, exp_title_3),
                        "&\\textsc{{{}}}\\\\\n".format(exp_employeur_3),
                        "&\small{{{}}}\\\\\n".format(exp_adresse_3),
                        "&\\\\\n",
                        "&{}, {}, {}\\\\\n".format(exp_main_task_3_1, exp_main_task_3_2, exp_main_task_3_3)]
                        #"\multicolumn{2}{c}{}\\\\\n"]
    lines_1ere_formation = ["\section{{{}}}\n".format(intitule_formations),
                            "\\begin{tabular}{rl}\n",
                            "{} - {}&{}\\\\\n".format(formation_date_start_year_1, formation_date_end_year_1, intitule_formation_1),
                            "&{}, {}\\\\\n".format(formation_lieu_1, formation_adresse_1)]
    lines_2e_formation = ["{} - {}&{}\\\\\n".format(formation_date_start_year_2, formation_date_end_year_2, intitule_formation_2),
                          "&{}, {}\\\\\n".format(formation_lieu_2, formation_adresse_2)]
    lines_3e_formation = ["{} - {}&{}\\\\\n".format(formation_date_start_year_3, formation_date_end_year_3, intitule_formation_3),
                          "&{}, {}\\\\\n".format(formation_lieu_3, formation_adresse_3)]
    lines_skills_hobbies = ["\section{{{}}}".format(intitule_skills),
                            "\\begin{tabular}{rl}\n",
                            "&{}\\\\\n".format(skill1),
                            "&{}\\\\\n".format(skill2),
                            "&{}\\\\\n".format(skill3),
                            "\end{tabular}\n",
                            "\section{{{}}}".format(intitule_hobbies),
                            "\\begin{tabular}{rl}\n",
                            "&{}\\\\\n".format(hobbie1),
                            "&{}\\\\\n".format(hobbie2),
                            "&{}\\\\\n".format(hobbie3),
                            "\end{tabular}\n"]
    with open('./{}/{}_professional.tex'.format(outputdir, intitule_cv), "w") as f:
        f.writelines(lines_start_1)
        if font == 'tgheros' or font == 'tgadventor':
            f.writelines('\\renewcommand{\\familydefault}{\sfdefault}\n')
        f.writelines(lines_start_2)
        f.writelines(lines_1er_emploi)
        if not exp_title_2:
            pass
        else:
            f.writelines("\multicolumn{2}{c}{}\\\\\n")
            f.writelines(lines_2e_emploi)
        if not exp_title_3:
            pass
        else:
            f.writelines("\multicolumn{2}{c}{}\\\\\n")
            f.writelines(lines_3e_emploi)
        f.writelines("\end{tabular}\n")
        f.writelines(lines_1ere_formation)
        if not intitule_formation_2:
            pass
        else:
            f.writelines("\multicolumn{2}{c}{}\\\\\n")
            f.writelines(lines_2e_formation)
        if not intitule_formation_3:
            pass
        else:
            f.writelines("\multicolumn{2}{c}{}\\\\\n")
            f.writelines(lines_3e_formation)
        f.writelines("\end{tabular}\n")
        f.writelines(lines_skills_hobbies)
        f.write("\end{document}")

def write_deedy(font):
    lines_start_1 = ["\documentclass[]{deedy-resume-openfont}\n",
                    "\usepackage{{{}}}\n".format(font),
                    "\usepackage[utf8]{inputenc}\n"]
    lines_start_2 = ["\\begin{document}\n",
                    "\\namesection{{{}}}{{{}}}{{{} | {}}}\n".format(nom, prenom, email, phone),
                    "\\begin{minipage}[t]{0.33\\textwidth}\n",]
    lines_1ere_formation = ["\section{{{}}}\n".format(intitule_formations),
                            "\subsection{{{}}}\n".format(intitule_formation_1),
                            "\descript{{{}}}\n".format(formation_date_start_year_1, formation_date_end_year_1),
                            "\location{{{}, {}}}\n".format(formation_lieu_1, formation_adresse_1),
                            "\sectionsep\n"]
    lines_2e_formation = [ "\subsection{{{}}}\n".format(intitule_formation_2),
                            "\descript{{{}}}\n".format(formation_date_start_year_2, formation_date_end_year_2),
                            "\location{{{}, {}}}\n".format(formation_lieu_2, formation_adresse_2),
                            "\sectionsep\n"]
    lines_3e_formation = [ "\subsection{{{}}}\n".format(intitule_formation_3),
                            "\descript{{{}}}\n".format(formation_date_start_year_3, formation_date_end_year_3),
                            "\location{{{}, {}}}\n".format(formation_lieu_3, formation_adresse_3),
                            "\sectionsep\n"]
    lines_1er_emploi = ["\section{{{}}}\n".format(intitule_exp),
                        "\\runsubsection{{{}}}\n".format(exp_title_1),
                        "\descript{{{} {} - {} {}}}\n".format(exp_date_start_month_1, exp_date_start_year_1, exp_date_end_month_1, exp_date_end_year_1),
                        "\location{{{}, {}}}\n".format(exp_employeur_1, exp_adresse_1),
                        "\sectionsep\n"]
    lines_2e_emploi = ["\\runsubsection{{{}}}\n".format(exp_title_2),
                        "\descript{{{} {} - {} {}}}\n".format(exp_date_start_month_2, exp_date_start_year_2, exp_date_end_month_2, exp_date_end_year_2),
                        "\location{{{}, {}}}\n".format(exp_employeur_2, exp_adresse_2),
                        "\sectionsep\n"]
    lines_3e_emploi = ["\\runsubsection{{{}}}\n".format(exp_title_3),
                        "\descript{{{} {} - {} {}}}\n".format(exp_date_start_month_3, exp_date_start_year_3, exp_date_end_month_3, exp_date_end_year_3),
                        "\location{{{}, {}}}\n".format(exp_employeur_3, exp_adresse_3),
                        "\sectionsep\n"]
    lines_skills_hobbies = ["\section{{{}}}\n".format(intitule_skills),
                            "\\begin{tabular}{rl}\n",
                            "&{}\\\\\n".format(skill1),
                            "&{}\\\\\n".format(skill2),
                            "&{}\\\\\n".format(skill3),
                            "\end{tabular}\n",
                            "\section{{{}}}\n".format(intitule_hobbies),
                            "\\begin{tabular}{rl}\n",
                            "&{}\\\\\n".format(hobbie1),
                            "&{}\\\\\n".format(hobbie2),
                            "&{}\\\\\n".format(hobbie3),
                            "\end{tabular}\n"]
    with open('./{}/{}_deedy_{}.tex'.format(outputdir, intitule_cv, font), "w") as f:
        f.writelines(lines_start_1)
        if font == 'tgheros' or font == 'tgadventor':
            f.writelines('\\renewcommand{\\familydefault}{\sfdefault}\n')
        f.writelines(lines_start_2)
        f.writelines(lines_1ere_formation)
        if not intitule_formation_2:
            pass
        else:
            f.writelines(lines_2e_formation)
        if not intitule_formation_3:
            pass
        else:
            f.writelines(lines_3e_formation)
        f.writelines("\end{minipage}\n")
        f.writelines("\hfill\n")
        f.writelines("\\begin{minipage}[t]{0.66\\textwidth}\n")
        f.writelines(lines_1er_emploi)
        if not exp_title_2:
            pass
        else:
            f.writelines(lines_2e_emploi)
        if not exp_title_3:
            pass
        else:
            f.writelines(lines_3e_emploi)
        f.writelines(lines_skills_hobbies)
        f.writelines("\end{minipage}\n")
        f.write("\end{document}")
# Read data
column_type = {'id_candidature':'object',
                'random':'int',
                'intitule_cv':'object',
                'phrase_pres':'object',
                'nom':'object',
                'prenom':'object',
                'candidat_adr':'object',
                'candidat_mail':'object',
                'candidat_tel':'object',
                'intitule_experiences':'object',
                'exp1_title':'object',
                'exp1_date_start_month':'object',
                'exp1_date_start_year':'object',
                'exp1_date_end_month':'object',
                'exp1_date_end_year':'object',
                'exp1_main_task1':'object',
                'exp1_main_task2':'object',
                'exp1_main_task3':'object',
                'exp1_employeur':'object',
                'exp1_adresse':'object',
                'exp2_title':'object',
                'exp2_date_start_month':'object',
                'exp2_date_start_year':'object',
                'exp2_date_end_month':'object',
                'exp2_date_end_year': 'object',
                'exp2_main_task1':'object',
                'exp2_main_task2':'object',
                'exp2_main_task3':'object',
                'exp2_employeur':'object',
                'exp2_adresse':'object',
                'exp3':'object',
                'exp3_date_start_month':'object',
                'exp3_date_start_year':'object',
                'exp3_date_end_month':'object',
                'exp3_date_end_year':'object',
                'exp3_main_task1':'object',
                'exp3_main_task2':'object',
                'exp3_main_task3':'object',
                'lieu_exp3':'object',
                'adr_exp3':'object',
                'intitule_formations':'object',
                'formation1':'object',
                'formation1_lieu':'object',
                'formation1_adr':'object',
                'formation1_date_start_year':'object',
                'formation1_end_start_year':'object',
                'formation2':'object',
                'formation2_lieu':'object',
                'formation2_adr':'object',
                'formation2_date_start_year':'object',
                'formation2_end_start_year':'object',
                'formation3':'object',
                'formation3_lieu':'object',
                'formation3_adr':'object',
                'formation3_date_start_year':'object',
                'formation3_end_start_year':'object',
                'intitule_skills':'object',
                'skill1':'object',
                'skill2':'object',
                'skill3':'object',
                'intitule_hobbies':'object',
                'hobbie1':'object',
                'hobbie2':'object',
                'hobbie3': 'object'}


if len(sys.argv[1:]) == 0:
    print 'Usage: resumes-combined.py -i <inputfile> [-o <outputdirectory>] [-l <layout>] [-f <font>]'
    sys.exit(2)

font = ''
layout = ''
outputdir = './output'
helpmessage = """Usage: resumes-combined.py -i <inputfile> [-o <outputdirectory>] [-l <layout>] [-f <font>]

    -i, --inputfile     Name of inputfile. Must be cvs format.
    -o, --outputdir     (Optional) Name of directory to which TeX files will be written. Will be created if inexistent.
    -l, --layout        (Optional) Name of desired layout. Must be one of: banking, classic, ecv, oldstyle, professional, academic, cleancv, deedy. Leaving this blank results in random layout.
    -f, --font          (Optional) Name of desired font. Must be one of: tgheros, tgbonum, tgtermes, tgadventor, lmodern, kpfonts. Leaving this blank results in default pairings. See README on Drive."""
    
try:
    opts, args = getopt.getopt(sys.argv[1:],"hi:o:l:f:",["inputfile=","outputdir=","layout=","font="])
except getopt.GetoptError:
    print helpmessage
    sys.exit(2)
for opt, arg in opts:
    if opt == '-h':
        print helpmessage
        sys.exit()
    elif opt in ("-i", "--ifile"):
        inputfile = arg
        if not os.path.exists(inputfile):
            print("Input file does not exist.")
            sys.exit(2)
        if not inputfile[-3:] == "csv":
            print("Input file must be csv.")
            sys.exit(2)
    elif opt in ("-o", "--ofile"):
        outputdir = arg
        if not os.path.isdir(outputdir):
            os.mkdir(outputdir, 0755)
    elif opt in ("-f", "--font"):
        font = arg
        if font not in ("tgheros", "tgbonum", "tgtermes", "tgadventor", "lmodern", "kpfonts"):
            print("Not a valid font.")
            sys.exit(2)
    elif opt in ("-l", "--layout"):
        layout = arg
        if arg not in ("ecv", "cvus", "deedy", "banking", "classic", "oldstyle", 
            "professional", "academic", "cleancv"):
            print("Not a valid layout.")
            sys.exit(2)

if not os.path.isdir(outputdir):
    os.mkdir(outputdir, 0755)

dt = pd.read_csv(inputfile, delimiter = ";", encoding = "latin3", dtype = column_type, keep_default_na = False)

print "Input file: ", inputfile
print "Output directory: ", outputdir
print "Layout: ", layout
print "Font: ", font

if font and layout:
    for i in range(0, len(dt.index)):
        read_data(data = dt, row = i)
        if layout == "banking":
            write_moderncv(layout  = "banking", font = font)
        elif layout == "classic":
            write_moderncv(layout  = "classic", font = font)
        elif layout == "oldstyle":
            write_moderncv(layout  = "oldstyle", font = font)
        elif layout == "professional":
            write_professional(font = font)
        elif layout == "academic":
            write_academic(font = font)
        elif layout == "ecv":
            write_ecv(font = font)
        elif layout == "cleancv":
            write_cleancv()
        elif layout == "deedy":
            write_deedy(font = font)
elif layout:
    for i in range(0, len(dt.index)):
        read_data(data = dt, row = i)
        if layout == "banking":
            write_moderncv(layout  = "banking", font = "tgheros")
        elif layout == "classic":
            write_moderncv(layout  = "classic", font = "tgbonum")
        elif layout == "oldstyle":
            write_moderncv(layout  = "oldstyle", font = "tgadventor")
        elif layout == "professional":
            write_professional(font = "lmodern")
        elif layout == "academic":
            write_academic(font = "kpfonts")
        elif layout == "ecv":
            write_ecv(font = "tgtermes")
        elif layout == "cleancv":
            write_cleancv()
        elif layout == "deedy":
            write_deedy(font = "lmodern")
elif font:
    for i in range(0, len(dt.index)):
        read_data(data = dt, row = i)
        branch = random.randint(1,8)
        print "Branch: ", branch
        if branch == 1:
            write_moderncv(layout  = "banking", font = font)
        elif branch == 2:
            write_moderncv(layout  = "classic", font = font)
        elif branch == 3:
            write_moderncv(layout  = "oldstyle", font = font)
        elif branch == 4:
            write_professional(font = font)
        elif branch == 5:
            write_academic(font = font)
        elif branch == 6:
            write_ecv(font = font)
        elif branch == 7:
            write_cleancv()
        elif branch == 8:
            write_deedy(font = font)
else:
    for i in range(0, len(dt.index)):
        read_data(data = dt, row = i)
        branch = random.randint(1,8)
        print "Branch: ", branch
        if branch == 1:
            write_moderncv(layout  = "banking", font = "tgheros")
        elif branch == 2:
            write_moderncv(layout  = "classic", font = "tgbonum")
        elif branch == 3:
            write_moderncv(layout  = "oldstyle", font = "tgadventor")
        elif branch == 4:
            write_professional(font = "lmodern")
        elif branch == 5:
            write_academic(font = "kpfonts")
        elif branch == 6:
            write_ecv(font = "tgtermes")
        elif branch == 7:
            write_cleancv()
        elif branch == 8:
            write_deedy(font = "lmodern")
