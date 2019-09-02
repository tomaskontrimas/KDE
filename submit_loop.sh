for i in 1.5 2.0 2.1 2.2 2.3 2.4 2.5 2.6 2.7 2.8 2.9 3.0 3.5
do
    #python submit_cv.py --adaptive --split --seed --weighting=plotter_wkde --gamma=$i --phi0=1.0 sig_psi_E
    #python submit_cv.py --adaptive --split --weighting=plotter_wkde --gamma=$i --phi0=1.0 sig_psi_E

    #python submit_cv.py --adaptive --split --weighting=plotter_wkde --gamma=$i --phi0=1.0 sig_dec_E
    #python submit_pdf.py --adaptive --weighting=plotter_wkde --gamma=$i --phi0=1.0 sig_dec_E

    #python submit_pdf.py --adaptive --weighting=plotter_wkde --gamma=$i --phi0=1.0 sig_E
   
    #python submit_pdf.py --adaptive --seed --weighting=plotter_wkde --gamma=$i --phi0=1.0 sig_psi_E
    #python submit_pdf.py --adaptive --weighting=plotter_wkde --gamma=$i --phi0=1.0 sig_psi_E

    #python submit_cv.py --adaptive --split --weighting=plotter_wkde --gamma=$i --phi0=1.0 bg
    #python submit_pdf.py --adaptive --weighting=plotter_wkde --gamma=$i --phi0=1.0 bg
    
    #python submit_cv.py --adaptive --split --weighting=plotter_wkde --gamma=$i --phi0=1.0 dec
    #python submit_pdf.py --adaptive --weighting=plotter_wkde --gamma=$i --phi0=1.0 dec

    python submit_cv.py --adaptive --split --nbins=100 --weighting=conv+pl --gamma=$i --phi0=1.0 bg
    #python submit_pdf.py --adaptive --weighting=conv+pl --gamma=$i --phi0=1.0 bg
done
