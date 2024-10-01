from gensim_analysis import *
from glide_analysis import *
from final_selection import *

if __name__ == "__main__":
    
    n = 'gensim_mt_sel'
    resdir = '/home/cactus/julia/gensim/selective/outer10'
    
    # GENSIM ANALYSIS
    """
    get_all_generated_molecules(results_dir=resdir, outname=n)
    
    create_table_gm_counts(results_dir=resdir, outname=n, save_df=True)
    
    plot_all_props_in_one(results_dir=resdir, save_fig=True)
    
    convert_csv_to_sdf_file(csv_to_convert='%s/all_generated_molecules.csv'%resdir, outdir=resdir)
    remove_duplicates_from_sdf(sdf_file='%s/all_generated_molecules.sdf'%resdir)
    """
    
    # GLIDE ANALYSIS
    """
    get_best_glide_docking_pose(csv_file='/home/cactus/julia/gensim/selective/glide10/docking/SARS2_7rnwA1.csv')
    get_best_glide_docking_pose(csv_file='/home/cactus/julia/gensim/selective/glide10/docking/SARS_2gx4A1.csv')
    get_best_glide_docking_pose(csv_file='/home/cactus/julia/gensim/selective/glide10/docking/MERS_7eneC1.csv')
    
    csvs = ['/home/cactus/julia/gensim/selective/glide10/docking/SARS2_7rnwA1_best.csv',\
            '/home/cactus/julia/gensim/selective/glide10/docking/SARS_2gx4A1_best.csv',\
            '/home/cactus/julia/gensim/selective/glide10/docking/MERS_7eneC1_best.csv']
    filter_by_glide_gscore_paninhibitors(list_of_csvs=csvs, outdir=resdir.replace('10', '11'), gscore_global=-8.2, gscore_individual=-7.7)
    """

    # get global gscores
    """
    for i in range(11):
        csvs = ['/home/cactus/julia/gensim/selective/glide%s/docking/SARS2_7rnwA1_best.csv'%i,\
                '/home/cactus/julia/gensim/selective/glide%s/docking/SARS_2gx4A1_best.csv'%i,\
                '/home/cactus/julia/gensim/selective/glide%s/docking/MERS_7eneC1_best.csv'%i]
        get_mean_glide_gscores(list_of_csv=csvs, out='/home/cactus/julia/gensim/selective/glide%s/docking/global_glide_best.csv'%i)
        print('Glide %s done.'%i)
    """

    # PLOT HISTOGRAMS OF GLIDE DOCKING SCORES
    """
    virus = 'SARS2'      # Select: 'SARS2', 'SARS', 'MERS', 'global'
    target = '7rnwA1'   # Select: '7rnwA1', '2gx4A1', '7eneC1', 'glide'
    glide_csvs = ['/home/cactus/julia/gensim/selective/glide0/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide1/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide2/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide3/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide4/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide5/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide6/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide7/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide8/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide9/docking/%s_%s_best.csv'%(virus,target),\
                    '/home/cactus/julia/gensim/selective/glide10/docking/%s_%s_best.csv'%(virus,target)]
    labels = ['initial', 'outer1', 'outer2', 'outer3', 'outer4', 'outer5', 'outer6', 'outer7', 'outer8', 'outer9', 'outer10']
    superimpose_histograms(list_of_csvs=glide_csvs, list_of_labels=labels, insert_title='Glide docking score', out='/home/cactus/julia/gensim/selective/plots/%s_hist_gscores.png'%virus, savefig=True, legend_loc='upper right')
    superimpose_histograms(list_of_csvs=glide_csvs, list_of_labels=labels, insert_title='Glide docking score', out='/home/cactus/julia/gensim/selective/plots/%s_hist_gscores_zoom.png'%virus, savefig=True, legend_loc='upper left', xlim=[-10.5,-7.5], ylim=[0, 500])
    """
    
    # TABLE OF THRESHOLD COUNTS
    """
    create_df_gscore_vs_tanimoto(files_dir='/home/cactus/julia/gensim/selective/', specific_set='/home/cactus/julia/gensim/selective/sel_init_spec_set.smi', virus=virus, target=target)
    
    tables = ['/home/cactus/julia/gensim/selective/SARS2_df_gscore_tanimoto.csv',\
                '/home/cactus/julia/gensim/selective/SARS_df_gscore_tanimoto.csv',\
                '/home/cactus/julia/gensim/selective/MERS_df_gscore_tanimoto.csv']
    glob_gscores = [-7, -7.5, -8, -8.5, -9, -9.5, -10]
    ind_gscores = [-6.5, -7, -7.5, -8, -8.5, -9, -9.5]
    for i in range(7):
        apply_thresholds(global_csv='/home/cactus/julia/gensim/selective/global_df_gscore_tanimoto.csv', individual_csvs=tables, 
                         gscore_ind=ind_gscores[i], gscore_glob=glob_gscores[i], tan_ind=1, tan_glob=1)
    """
    
    # PLOT SPECIFIC SET EVOLUTION
    """
    plot_specific_set_evolution(results_dir='/home/cactus/julia/gensim/selective',\
                                outdir='/home/cactus/julia/gensim/selective/plots', outname='specific_set_evolution')
    """
    
    # PLOT TSNEs
    # by inner loop
    """
    _simplify_specific_sets(results_dir=resdir, outname=n)
    spec_simples = glob.glob('%s/%s_*/%s_specific_smiles_simple.csv'%(resdir, n, n))
    spec_inner = [x.split('/')[-2].split('_')[-1] for x in spec_simples]
    for i, spec_simple in enumerate(spec_simples):
        convert_csv_to_sdf_file(csv_to_convert=spec_simple, outdir='%s/%s_%s'%(resdir, n, spec_inner[i]), inner=spec_inner[i])

    spec_simples = glob.glob('%s/%s_*/%s_specific_smiles_simple.sdf'%(resdir, n, n))
    sdf_list = []
    rev_inners = list(range(1, len(spec_simples)+1))
    rev_inners.sort(reverse=True)
    for i in rev_inners:
        sdf_list.append('/home/cactus/julia/gensim/full/outer1/gensim_mt_%s/gensim_mt_specific_smiles_simple.sdf'%i)
    names = ['specific_19', 'specific_18', 'specific_17', 'specific_16', 'specific_15',\
            'specific_14', 'specific_13', 'specific_12', 'specific_11', 'specific_10',\
            'specific_9', 'specific_8', 'specific_7', 'specific_6', 'specific_5',\
            'specific_4', 'specific_3', 'specific_2', 'specific_1', 'specific_0']
    sizes = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6]
    alphas = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
    markers = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "o", "*"]
    plot_modbs_tSNE_or_UMAP(list_of_sdfs=sdf_list, list_of_names=names, outdir='/home/cactus/julia/gensim/selective/outer10', outname='UMAP_outer10',\
                            sizes=sizes, alphas=alphas, markers=markers, ptype='UMAP')
    """
    # by outer loop
    """
    sdf_list = glob.glob('/home/cactus/julia/gensim/selective/outer?/sel_spec_set_outer?.smi')
    sdf_list.sort()
    sdf_list.append('/home/cactus/julia/gensim/selective/outer10/sel_spec_set_outer10.smi')
    sdf_list.insert(0, '/home/cactus/julia/gensim/selective/sel_init_spec_set.smi')   
    simplify_specific_sets_smi(list_spec_set=sdf_list)
    """
    """
    sdf_list = glob.glob('/home/cactus/julia/gensim/selective/outer?/sel_spec_set_outer?_simple.smi')
    sdf_list.sort(reverse=True)
    sdf_list.insert(0, '/home/cactus/julia/gensim/selective/outer10/sel_spec_set_outer10_simple.smi')
    sdf_list.append('/home/cactus/julia/gensim/selective/sel_init_spec_set.smi')

    names = ['outer10', 'outer9', 'outer8', 'outer7', 'outer6', 'outer5', 'outer4', 'outer3', 'outer2', 'outer1']
    sizes = [0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4]
    alphas = [0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9]
    markers = ["o", "o", "o", "o", "o", "o", "o", "o", "o", "*"]
    
    plot_UMAP(list_smis=sdf_list, list_names=names, outdir='/home/cactus/julia/gensim/selective/plots', outname='UMAP_spec_sets',\
              sizes=sizes, alphas=alphas, markers=markers)
    """
    
    
    # PLOT GSCORE VS. TANIMOTO
    """
    virus = 'global'      # Select: 'SARS2', 'SARS', 'MERS', 'global'
    plot_gscore_vs_tanimoto(csv_file='/home/cactus/julia/gensim/selective/%s_df_gscore_tanimoto.csv'%virus,\
                            outdir='/home/cactus/julia/gensim/selective/plots', outname='%s_scatter_gscore_tanimoto'%virus,\
                            gscore_threshold=-8, tan_threshold=0.3,\
                            save_csv=False, plot_max_lim=[-7, 0.5])
    """
    
    # PLOT CUMULATIVE HISTOGRAMS OF GSCORES
    """
    virus = 'global'      # Select: 'SARS2', 'SARS', 'MERS', 'global'
    target = 'glide'   # Select: '7rnwA1', '2gx4A1', '7eneC1', 'glide'
    cumulative_histograms(final_csvs=['/home/cactus/julia/gensim/full/%s_df_gscore_tanimoto.csv'%virus, \
                          '/home/cactus/julia/gensim/selective/%s_df_gscore_tanimoto.csv'%virus],\
                          initial_csvs=['/home/cactus/julia/gensim/full/glide0/docking/%s_%s_docking_best.csv'%(virus,target),\
                          '/home/cactus/julia/gensim/selective/glide0/docking/%s_%s_best.csv'%(virus,target)],\
                          list_of_labels = ['generated FULL', 'generated SELECTIVE', 'initial FULL', 'initial SELECTIVE'],\
                          list_of_colors = ['lightgreen', 'cornflowerblue', 'red', 'darkred'], insert_title='Glide docking score',\
                          out='/home/cactus/julia/gensim/Mpro_GMN/plots/%s_cum_hist_gscores.png'%virus, savefig=True, legend_loc='upper right', xlim=None, ylim=None)
    cumulative_histograms(final_csvs=['/home/cactus/julia/gensim/full/%s_df_gscore_tanimoto.csv'%virus, \
                          '/home/cactus/julia/gensim/selective/%s_df_gscore_tanimoto.csv'%virus],\
                          initial_csvs=['/home/cactus/julia/gensim/full/glide0/docking/%s_%s_docking_best.csv'%(virus,target),\
                          '/home/cactus/julia/gensim/selective/glide0/docking/%s_%s_best.csv'%(virus,target)],\
                          list_of_labels = ['generated FULL', 'generated SELECTIVE', 'initial FULL', 'initial SELECTIVE'],\
                          list_of_colors = ['lightgreen', 'cornflowerblue', 'red', 'darkred'], insert_title='Glide docking score',\
                          out='/home/cactus/julia/gensim/Mpro_GMN/plots/%s_cum_hist_gscores_zoom.png'%virus, savefig=True, legend_loc='upper left', xlim=[-10.5, -7.5], ylim=[0, 2500])
    """
    
    # FINAL SELECTION FOR PELE
    """
    tables = ['/home/cactus/julia/gensim/selective/SARS2_df_gscore_tanimoto.csv',\
                '/home/cactus/julia/gensim/selective/SARS_df_gscore_tanimoto.csv',\
                '/home/cactus/julia/gensim/selective/MERS_df_gscore_tanimoto.csv']
    glob_gscores = [-7, -7.5, -8, -8.5, -9, -9.5, -10]
    ind_gscores = [-6.5, -7, -7.5, -8, -8.5, -9, -9.5]
    for i in range(7):
        apply_thresholds(global_csv='/home/cactus/julia/gensim/selective/global_df_gscore_tanimoto.csv', individual_csvs=tables, 
                         gscore_ind=ind_gscores[i], gscore_glob=glob_gscores[i], tan_ind=0.3, tan_glob=0.3)
    """
    
    """

    # GET TABLE OF RESULTS
    map_gscores_generated(csv_global='/home/cactus/julia/gensim/selective/global_df_gscore_tanimoto.csv',\
                            csv_virus=['/home/cactus/julia/gensim/selective/SARS2_df_gscore_tanimoto.csv',\
                            '/home/cactus/julia/gensim/selective/SARS_df_gscore_tanimoto.csv',\
                            '/home/cactus/julia/gensim/selective/MERS_df_gscore_tanimoto.csv'],\
                            outdir='/home/cactus/julia/gensim/selective', outname='results')
    
    """
    # CLUSTER DBSCANS
    """

    plot_cluster_DBSCAN(csv_results='/home/cactus/julia/gensim/selective/results.csv',
                        smi_specific='/home/cactus/julia/gensim/selective/sel_init_spec_set.smi',
                        gscore_glob_thr=-8,
                        gscore_ind_thr=-7.5,
                        tanimoto_thr=0.3,
                        similarity_thrs=[0.7, 0.6, 0.5, 0.4, 0.3],
                        outname='plots/cluster_dbscans_selective')

    plot_new_scaffolds(csv_results='/home/cactus/julia/gensim/selective/results.csv',
                       smi_specific='/home/cactus/julia/gensim/selective/sel_init_spec_set.smi',
                       gscore_glob_thr=-8,
                       gscore_ind_thr=-7.5,
                       tanimoto_thr=0.3,
                       similarity_thrs=[0.7, 0.6, 0.5, 0.4, 0.3],
                       outname='plots/perc_newscaffolds_selective')
    """

    virus = 'SARS2'      # Select: 'SARS2', 'SARS', 'MERS', 'global'
    target = '7rnwA1'   # Select: '7rnwA1', '2gx4A1', '7eneC1', 'glide'
    create_df_gscore_vs_tanimoto(files_dir='/home/cactus/julia/gensim/selective/',
                                 specific_set='/home/cactus/julia/gensim/selective/sel_init_spec_set.smi',
                                 virus=virus,
                                 target=target)

    exit()
    indv = -9
    glob = -9.5
    csv_results = '/home/cactus/julia/gensim/selective/results.csv'
    df = pd.read_csv(csv_results)
    df_filt = df[(df['global_gscore'] <= glob) & (df['gscore_SARS2'] <= -indv) & (df['gscore_SARS'] <= indv) & (df['gscore_MERS'] <= indv)  & (df['max_tan'] <= 0.3)]
    print(df_filt)
    df_filt.to_csv('test.csv')