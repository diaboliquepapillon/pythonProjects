import random
import os
from prettytable import PrettyTable
from termcolor import colored, cprint
def clear_screen():
  try:
    os.system('cls')
  except:
    os.system('clear')

countries = {'Africa': {'Algeria': 'Algiers|43,851,044',
  'Angola': 'Luanda|32,866,272',
  'Benin': 'Porto-Novo|12,123,200',
  'Botswana': 'Gaborone|2,351,627',
  'Burkina Faso': 'Ouagadougou|20,903,273',
  'Burundi': 'Gitega|11,890,784',
  'Cabo Verde': 'Praia|555,987',
  'Cameroon': 'Yaounde|26,545,863',
  'Central African Republic': 'Bangui|4,829,767',
  'Comoros': 'Moroni|869,601',
  'Democratic Republic of the Congo': 'Kinshasa|89,899,332',
  'Republic of the Congo': 'Brazzaville|5,244,359',
  'Djibouti': 'Djibouti|988,000',
  'Egypt': 'Cairo|102,334,404',
  'Equatorial Guinea': 'Malabo|1,402,985',
  'Eritrea': 'Asmara|3,546,421',
  'Eswatini (formerly Swaziland)': 'Mbabane|1,160,164',
  'Ethiopia': 'Addis Ababa|114,963,588',
  'Gabon': 'Libreville|2,225,734',
  'Gambia': 'Banjul|2,416,668',
  'Ghana': 'Accra|31,072,940',
  'Guinea': 'Conakry|13,132,795',
  'Guinea-Bissau': 'Bissau|1,968,001',
  'Kenya': 'Nairobi|53,771,296',
  'Lesotho': 'Maseru|2,142,249',
  'Liberia': 'Monrovia|5,057,681',
  'Libya': 'Tripoli|6,871,292',
  'Madagascar': 'Antananarivo|27,691,018',
  'Malawi': 'Lilongwe|19,129,952',
  'Mali': 'Bamako|20,250,833',
  'Mauritania': 'Nouakchott|4,649,658',
  'Mauritius': 'Port Louis|1,271,768',
  'Morocco': 'Rabat|36,910,560',
  'Mozambique': 'Maputo|31,255,435',
  'Namibia': 'Windhoek|2,540,905',
  'Niger': 'Niamey|24,206,644',
  'Nigeria': 'Abuja|206,139,589',
  'Rwanda': 'Kigali|12,952,218',
  'Sao Tome and Principe': 'São Tomé|211,028',
  'Senegal': 'Dakar|16,743,927',
  'Seychelles': 'Victoria|98,347',
  'Sierra Leone': 'Freetown|7,976,983',
  'Somalia': 'Mogadishu|15,893,222',
  'South Africa': 'Cape Town|59,308,690',
  'South Sudan': 'Juba|11,193,725',
  'Sudan': 'Khartoum|43,849,260',
  'Tanzania': 'Dodoma|59,734,218',
  'Togo': 'Lomé|8,278,724',
  'Tunisia': 'Tunis|11,818,619',
  'Uganda': 'Kampala|45,741,007',
  'Zambia': 'Lusaka|18,383,955',
  'Zimbabwe': 'Harare|14,862,924'},
 'Asia': {'Afghanistan': 'Kabul|38,928,346',
  'Armenia': 'Yerevan|2,963,243',
  'Azerbaijan': 'Baku|10,139,177',
  'Bahrain': 'Manama|1,701,575',
  'Bangladesh': 'Dhaka|164,689,383',
  'Bhutan': 'Thimphu|771,608',
  'Brunei': 'Bandar Seri Begawan|437,479',
  'Cambodia': 'Phnom Penh|16,718,965',
  'China': 'Beijing|1,439,323,776',
  'Cyprus': 'Nicosia|1,207,359',
  'Georgia': 'Tbilisi|3,989,167',
  'India': 'New Delhi|1,380,004,385',
  'Indonesia': 'Jakarta|273,523,615',
  'Iran': 'Tehran|83,992,949',
  'Iraq': 'Baghdad|40,222,493',
  'Israel': 'Jerusalem|8,655,535',
  'Japan': 'Tokyo|126,476,461',
  'Jordan': 'Amman|10,203,134',
  'Kazakhstan': 'Nur-Sultan|18,776,707',
  'Kuwait': 'Kuwait City|4,270,571',
  'Kyrgyzstan': 'Bishkek|6,524,195',
  'Laos': 'Vientiane|7,275,560',
  'Lebanon': 'Beirut|6,825,445',
  'Malaysia': 'Kuala Lumpur|32,365,999',
  'Maldives': 'Male|540,544',
  'Mongolia': 'Ulaanbaatar|3,278,290',
  'Myanmar (formerly Burma)': 'Naypyidaw|54,409,800',
  'Nepal': 'Kathmandu|29,136,808',
  'North Korea': 'Pyongyang|25,778,816',
  'Oman': 'Muscat|5,106,626',
  'Pakistan': 'Islamabad|220,892,340',
  'Palestine': 'Jerusalem|5,101,414',
  'Philippines': 'Manila|109,581,078',
  'Qatar': 'Doha|2,881,053',
  'Russia': 'Moscow|145,934,462',
  'Saudi Arabia': 'Riyadh|34,813,871',
  'Singapore': 'Singapore|5,850,342',
  'South Korea': 'Seoul|51,269,185',
  'Sri Lanka': 'Sri Jayawardenepura Kotte|21,413,249',
  'Syria': 'Damascus|17,500,658',
  'Taiwan': 'Taipei|23,816,775',
  'Tajikistan': 'Dushanbe|9,537,645',
  'Thailand': 'Bangkok|69,799,978',
  'Timor-Leste': 'Dili|1,318,445',
  'Turkey': 'Ankara|84,339,067',
  'Turkmenistan': 'Ashgabat|6,031,200',
  'United Arab Emirates': 'Abu Dhabi|9,890,402',
  'Uzbekistan': 'Tashkent|33,469,203',
  'Vietnam': 'Hanoi|97,338,579'},
 'Australia': {'Australia': 'Canberra|25,499,884',
  'Fiji': 'Suva|896,445',
  'Kiribati': 'Tarawa|119,449',
  'Marshall Islands': 'Majuro|59,190',
  'Micronesia': 'Palikir|115,023',
  'Nauru': 'Yaren|10,824',
  'New Zealand': 'Wellington|4,822,233',
  'Palau': 'Ngerulmud|18,094',
  'Papua New Guinea': 'Port Moresby|8,947,024',
  'Samoa': 'Apia|198,414',
  'Solomon Islands': 'Honiara|686,884',
  'Tonga': 'Nukuʻalofa|105,695',
  'Tuvalu': 'Funafuti|11,792',
  'Vanuatu': 'Port Vila|307,145'},
 'Europe': {'Albania': 'Tirana|2,877,797',
  'Andorra': 'Andorra la Vella|77,265',
  'Armenia': 'Yerevan|2,963,243',
  'Austria': 'Vienna|9,006,398',
  'Azerbaijan': 'Baku|10,139,177',
  'Belarus': 'Minsk|9,449,323',
  'Belgium': 'Brussels|11,589,623',
  'Bosnia and Herzegovina': 'Sarajevo|3,280,819',
  'Bulgaria': 'Sofia|6,948,445',
  'Croatia': 'Zagreb|4,105,267',
  'Cyprus': 'Nicosia|1,207,359',
  'Czechia': 'Prague|10,711,506',
  'Denmark': 'Copenhagen|5,792,202',
  'Estonia': 'Tallinn|1,326,535',
  'Finland': 'Helsinki|5,540,720',
  'France': 'Paris|65,273,511',
  'Georgia': 'Tbilisi|3,989,167',
  'Germany': 'Berlin|83,783,942',
  'Greece': 'Athens|10,423,054',
  'Hungary': 'Budapest|9,660,351',
  'Iceland': 'Reykjavik|341,243',
  'Ireland': 'Dublin|4,937,786',
  'Italy': 'Rome|60,461,826',
  'Kazakhstan': 'Nur-Sultan|18,776,707',
  'Kosovo': 'Pristina|1,870,981',
  'Latvia': 'Riga|1,886,198',
  'Liechtenstein': 'Vaduz|38,128',
  'Lithuania': 'Vilnius|2,722,289',
  'Luxembourg': 'Luxembourg|625,978',
  'Malta': 'Valletta|441,543',
  'Moldova': 'Chisinau|4,033,963',
  'Monaco': 'Monaco|39,242',
  'Montenegro': 'Podgorica|628,066',
  'Netherlands': 'Amsterdam|17,134,872',
  'North Macedonia (formerly Macedonia)': 'Skopje|2,083,363',
  'Norway': 'Oslo|5,421,241',
  'Poland': 'Warsaw|37,846,611',
  'Portugal': 'Lisbon|10,196,709',
  'Romania': 'Bucharest|19,237,691',
  'Russia': 'Moscow|145,934,462',
  'San Marino': 'San Marino|33,931',
  'Serbia': 'Belgrade|8,737,371',
  'Slovakia': 'Bratislava|5,459,642',
  'Slovenia': 'Ljubljana|2,078,938',
  'Spain': 'Madrid|46,754,778',
  'Sweden': 'Stockholm|10,099,265',
  'Switzerland': 'Bern|8,654,622',
  'Turkey': 'Ankara|84,339,067',
  'Ukraine': 'Kyiv|43,733,762',
  'United Kingdom': 'London|67,886,011',
  'Vatican City (Holy See)': 'Vatican City|825'},
 'North America': {'Bahamas': 'Nassau|393,244',
  'Barbados': 'Bridgetown|287,375',
  'Belize': 'Belmopan|397,628',
  'Canada': 'Ottawa|37,742,154',
  'Costa Rica': 'San Jose|5,094,118',
  'Cuba': 'Havana|11,326,616',
  'Dominica': 'Roseau|71,986',
  'Dominican Republic': 'Santo Domingo|10,847,910',
  'El Salvador': 'San Salvador|6,486,205',
  'Guatemala': 'Guatemala City|17,915,568',
  'Haiti': 'Port-au-Prince|11,402,528',
  'Honduras': 'Tegucigalpa|9,904,607',
  'Jamaica': 'Kingston|2,961,167',
  'Mexico': 'Mexico City|128,932,753',
  'Nicaragua': 'Managua|6,624,554',
  'Panama': 'Panama City|4,314,767',
  'Saint Kitts and Nevis': 'Basseterre|52,441',
  'Saint Lucia': 'Castries|183,627',
  'Saint Vincent and the Grenadines': 'Kingstown|110,210',
  'Trinidad and Tobago': 'Port of Spain|1,399,488',
  'United States of America': 'Washington, D.C.|330,123,605'},
 'South America': {'Argentina': 'Buenos Aires|45,195,774',
  'Bolivia': 'Sucre|11,673,021',
  'Brazil': 'Brasilia|212,559,417',
  'Chile': 'Santiago|19,116,201',
  'Colombia': 'Bogotá|50,882,891',
  'Ecuador': 'Quito|17,643,054',
  'Guyana': 'Georgetown|786,552',
  'Paraguay': 'Asunción|7,132,538',
  'Peru': 'Lima|32,971,854',
  'Suriname': 'Paramaribo|586,632',
  'Uruguay': 'Montevideo|3,473,730',
  'Venezuela': 'Caracas|28,435,940'}}

def Game():
  player_name = input("Hello, What's your name? ")
  clear_screen()
  def admin_menu():
    clear_screen()
    print(colored(f'Welcome {user_name}! This is Admin Panel.\nA. Remove Country/Capital pair\nB. Add Country/Capital pair.\nC. See the list\nD. Logout\nE. Exit', 'magenta'))
    return input(colored('Enter your choice: '))

  def main_menu():
    print(colored(f'Okay {player_name}, This is Capitals Guessing Game.','cyan'))
    print(colored('For every correct answer you are going to receive +10 points and for a wrong one -10.', 'cyan'))
    table = PrettyTable(['Choice', 'Description'])
    table.add_row(['A.', 'Admin Panel'])
    table.add_row(['B.','Play the Game'])
    table.add_row(['C.','Exit'])
    cprint(table,'magenta')
    return input('Enter your choice: ')


  selected_option = main_menu()
  points = 0

  if selected_option.lower() == 'a':
      print('Please provide username and password for Admin Panel.')
      user_name = input('Username: ')
      password = input('Password: ')
      if user_name.lower() == 'admin' and password == 'admin':
          selected_option == ''
          while selected_option.lower() != 'e' or selected_option.lower() != 'd':
              selected_option = admin_menu()
              if selected_option.lower() == 'a':
                  country = input('Enter country name: ')
                  for continent in countries:
                      try:
                          del countries[continent][country]
                      except:
                          pass
              elif selected_option.lower() == 'b':
                  continent = input('Enter continent: ')
                  country = input('Enter country: ')
                  capital = input('Enter capital: ')
                  try:
                      countries[continent][country] = capital
                  except:
                      print('Invalid continent name.')
              elif selected_option.lower() == 'c':
                output = PrettyTable(['Country', 'Capital/Population', 'Continents'])
                for continent in countries:
                      for country in countries[continent]:
                        output.add_row([country,countries[continent][country],continent])
                cprint(output,'green')
                input('Press any key to return to menu...')
              elif selected_option.lower() == 'd':
                  Game()
              elif selected_option.lower() == 'e':
                  print('Goodbye!')
                  break
      else:
        print('\a')
        print('Username and/or password is incorrect.')
  elif selected_option.lower() == 'b':
    while True:
      already_asked_countries = []
      rounds = 5
      continent_names = list(countries.keys())
      n = 1
      table = PrettyTable(['Choice', 'Description'])
      for name in continent_names:
        table.add_row([f'{n}.', name])
        n += 1
      table.add_row(['7.', 'Worldwide'])
      table.add_row(['8.', 'Go back to Menu'])
      table.add_row(['9.', 'Exit'])
      cprint(table, 'green')
      selected_option = int(input('Enter the area where you want to play in: '))
      if selected_option >= 1 and selected_option <= 6:
          selected_region = list(countries.keys())[selected_option - 1]
          print(f'You are now playing in {selected_region}')
          i = 1
          while i <= rounds:
            while True:
              country = random.choice(list(countries[selected_region]))
              if country not in already_asked_countries:
                break
            capital = countries[selected_region][country]
            population = capital.split('|')[1]
            print(f'\nQuestion # {i} What is the capital of {country}?')
            already_asked_countries.append(country)
            answer = input('Please type your answer:')
            if answer and answer.lower() in capital.lower():
              print('You have guessed correctly!')
              points += 10
            else:
              print('\a')
              print('Sorry the correct answer is', capital.split('|')[0])
              points -= 10
            if points < 0: points = 0
            i += 1
            print(f'Fun fact: The population of {country} is {population}\nYour score so far is {points}')
          print(f'You got {points} points')
      elif selected_option == 7:
        already_asked_countries = []
        all_countries = {}
        for continent in countries:
          all_countries.update(countries[continent])
        i = 1
        while i <= rounds:
          while True:
            country = random.choice(list(all_countries.keys()))
            if country not in already_asked_countries:
              break
          capital = all_countries[country]
          population = capital.split('|')[1]
          print(f'\nQuestion # {i} What is the capital of {country}?')
          already_asked_countries.append(country)
          answer = input('Please type your answer:')
          if answer and answer.lower() in capital.lower():
            print('You have guessed correctly!')
            points += 10
          else:
            print('\a')
            print('Sorry the correct answer is', capital.split('|')[0])
            points -= 10
          if points < 0: points = 0
          i += 1 
          print(f'Fun fact: The population of {country} is {population}\nYour score so far is {points}')
        print(f'You got {points} points')
      elif selected_option == 8:
        Game()
      elif selected_option == 9:
        print('Goodbye!')
        break

  elif selected_option.lower() == 'c':
    print('Goodbye!')
    return
  else:
    print('\a')
    cprint('\t\tInvalid Value', 'red')

Game()