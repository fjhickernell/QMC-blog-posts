
pyreverse -k qmcpy/ --ignore util,integrand,true_measure,discrete_distribution; mv classes.dot ./uml/qmcpy_blog_uml3.dot
# removed 3, 4, 5, 6
dot -Tpng  ./uml/qmcpy_blog_uml3.dot > ./uml/qmcpy_blog_uml3.png

#	Accumulate Data
pyreverse qmcpy/accumulate_data/ --ignore=mean_var_data.py,mean_var_data_rep.py  -o png 1>/dev/null && mv classes.png ./uml/accumulate_data_blog_uml.png
#	Discrete Distribution
pyreverse qmcpy/discrete_distribution/ --ignore=korobov.py,halton.py -o png 1>/dev/null && mv classes.png ./uml/discrete_distribution_blog_uml.png
#	Integrand
pyreverse qmcpy/integrand/ --ignore=linear0.py -o png 1>/dev/null && mv classes.png ./uml/integrand_blog_uml.png
#	Stopyreverse qmcpy/integrand/pping Criterion
pyreverse qmcpy/stopping_criterion/ --ignore=cub_mc_g.py,cub_mc_ml_cont.py,cub_mc_clt.py,cub_qmc_lattice_g.py,cub_qmc_ml_cont.py,cub_qmc_bayes_lattice_g.py,cub_mc_ml.py   -o png 1>/dev/null && mv classes.png ./uml/stopping_criterion_blog_uml.png
