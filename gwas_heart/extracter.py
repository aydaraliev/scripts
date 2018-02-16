import pandas as pd

gwas = pd.read_csv("./gwas_catalog_v1.0-associations_e91_r2018-02-06.tsv", sep='\t')

#stroke
stroke = gwas[(gwas['DISEASE/TRAIT'] == 'Ischemic stroke')]
#heart
heart = gwas[(gwas['DISEASE/TRAIT'] == 'Coronary heart disease') |
             (gwas['DISEASE/TRAIT'] == 'Coronary artery disease')]

def filter_e8(data):
    data['P-VALUE'] = data['P-VALUE'].apply(pd.to_numeric, args=('raise',))
    data = data[data['P-VALUE'] <= 5e-8]
    data = data.sort_values('P-VALUE', ascending=True).reset_index()
    return data

def filter_e5_2ormore(data):
    data = data[data['P-VALUE'] <= 5e-5]
    data = data.sort_values('P-VALUE', ascending=True).reset_index()
    counts = data['SNPS'].value_counts()
    counts_series = pd.Series(counts[counts>=2].index)
    data = data[data['SNPS'].isin(counts_series)]
    data = data.sort_values('SNPS')
    return data

if __name__ == "__main__":

    stroke_e8 = filter_e8(stroke)
    stroke_2_or_more = filter_e5_2ormore(stroke)
    heart_e8 = filter_e8(heart)
    heart_2_or_more = filter_e5_2ormore(heart)
    stroke_e8.to_excel("stroke_e8.xlsx")
    stroke_2_or_more.to_excel('stroke_e5_2_or_more.xlsx')
    heart.to_excel("heart_e8.xlsx")
    heart_2_or_more.to_excel('heart_e5_2_or_more.xlsx')






''''#stroke to excel
#e8
stroke['P-VALUE'] = stroke['P-VALUE'].apply(pd.to_numeric, args=('raise',))
stroke_pval5xe8 = stroke[stroke['P-VALUE'] <= 5e-8]
stroke_pval5xe8 = stroke_pval5xe8.sort_values('P-VALUE', ascending=True).reset_index()
#writing
stroke_pval5xe8.to_excel("stroke_e8.xlsx")
#e5
stroke_pval5xe5 = stroke[stroke['P-VALUE'] <= 5e-5]
stroke_pval5xe5 = stroke_pval5xe5.sort_values('P-VALUE', ascending=True).reset_index()
counts5xe5 = stroke_pval5xe5['SNPS'].value_counts()
stroke_rs_more_than_2 = pd.Series(counts5xe5[counts5xe5 >= 2].index)
stroke_pval5xe5_more_than_2 = stroke_pval5xe5[stroke_pval5xe5['SNPS'].isin(stroke_rs_more_than_2)]
#writing
stroke_pval5xe5_more_than_2.to_excel('stroke_e5_2_or_more.xlsx')

#heart to excel
#e8
heart['P-VALUE'] = heart['P-VALUE'].apply(pd.to_numeric, args=('raise',))
heart_pval5xe8 = heart[heart['P-VALUE'] <= 5e-8]
heart_pval5xe8 = heart_pval5xe8.sort_values('P-VALUE', ascending=True).reset_index()
#writing
heart_pval5xe8.to_excel("heart_e8.xlsx")
#e5
heart_pval5xe5 = heart[heart['P-VALUE'] <= 5e-5]
heart_pval5xe5 = heart_pval5xe5.sort_values('P-VALUE', ascending=True).reset_index()
counts5xe5 = heart_pval5xe5['SNPS'].value_counts()
heart_rs_more_than_2 = pd.Series(counts5xe5[counts5xe5 >= 2].index)
heart_pval5xe5_more_than_2 = heart_pval5xe5[heart_pval5xe5['SNPS'].isin(stroke_rs_more_than_2)]
#writing
heart_pval5xe5_more_than_2.to_excel('heart_e5_2_or_more.xlsx')'''