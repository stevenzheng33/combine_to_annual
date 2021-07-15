 time_list =['12','11','10','9','8','7','3','2']
 buy_or_sell = '购方'
 year = '2019'
def combine_monthly(time_list,buy_or_sell,year)
    df = pd.DataFrame(columns=['市场成员']) 
    suffix = tuple(time_list)
    for i in time_list:
        cur_df = pd.read_excel(year+'_'+i+'_'+buy_or_sell+'.xls')[['市场成员',buy_or_sell+'电量']]
        cur_df = cur_df.iloc[:-1,:]
        print(cur_df)
        df = df.merge(cur_df, on='市场成员', how='outer')