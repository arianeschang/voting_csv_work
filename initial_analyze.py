import pandas as pd

def main():

	df_addresses = pd.read_csv('addresses.csv')
	df_pp_list = pd.read_csv('precinct_polling_list.csv')

	df_pp_list[['State', 'ZIP']] = df_pp_list['State/ZIP'].str.split(' ', expand = True)
	df_pp_list = df_pp_list.drop('State/ZIP', 1)

	print df_pp_list
	print df_addresses

if __name__ == "__main__":
    main()