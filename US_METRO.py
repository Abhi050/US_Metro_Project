import time
import pandas as pd
import numpy as np
import datetime as dt

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('\n')
    i=1
    print('Hi my name is Abhishek.\n Iam here to help you with US Metro data.\n')
    while i>0:

        city = (input("For which city do u want to look data for?\n(1.)Chicago\n(2.)New York\n(3.)Washington\n\n")).lower()
        if city == "chicago":

            a='chicago.csv'
            i=0
        elif city == 'new york':
            a= 'new_york_city.csv'
            i=0
        elif city == 'washington':
            a= 'washington.csv'
            i=0
        else:
            print('Wrong Input')
            i=1




    # get user input for month (all, january, february, ... , june)
    print('Now Enetr the name of the month for which you want to see the data\n')
    print('Choose from the following:\n')
    print('all,January, February, March, April, May, or June')
    print("Enetr your choice:\n")
    i=1
    while i>0:

        month=input(":-")
        if month == 'january':

            b= 1
            i=0
        elif month == 'february':
            b= 2
            i=0
        elif month == 'march':
            b= 3
            i=0
        elif month == 'april':
            b= 4
            i=0
        elif month == 'may':
            b= 5
            i=0
        elif month == 'june':
            b= 6
            i=0
        elif month == 'all':
            b= 7
            i=0
        else:
            print('Wrong choice try again')
            i=1

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('Now Enter the day of the week for which you are looking for\n')
    print('Choose from :\n')
    print('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all\n')
    i=1
    while i!=0:
        day =(input(":-")).lower()
        if day == 'monday':
            c= 1
            i=0
        elif day == 'tuesday':
            c= 2
            i=0
        elif day == 'wednesday':
            c= 3
            i=0
        elif day == 'thursday':
            c= 4
            i=0
        elif day == 'friday':
            c= 5
            i=0
        elif day == 'saturday':
            c= 6
            i=0
        elif day == 'sunday':
            c= 7
            i=0
        elif day == 'all':
            c= 8
            i=0
        else:
            print('wrong choice .Try again\n')
            i=1



    print('-'*40)
    return a,b,c


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    city=pd.read_csv(city)
    city['Start Time'] = pd.to_datetime(city['Start Time'])
    city['month']=city['Start Time'].dt.month
    city['day']=city['Start Time'].dt.weekday_name


    days =['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    if month != 7:
        b=city[city['month'] == month]
    else:
        b=city
    if day !=8:
        df=b[city['day'] == days[day-1]]
    else:
        df=b




    return df,b


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    m2=['January','February','March','April','May','June']
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    popular_month =[df['month'].mode()[0]]



    print('\n\nThe most common month is\n')
    print(":-")
    print(popular_month)



    # display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['day'] = df['Start Time'].dt.dayofweek


    popular_day = df['day'].mode()[0]
    print('\n\nThe most common day of the week is\n')
    print(":-")
    print(popular_day)



    # display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['hour'] = df['Start Time'].dt.hour


    popular_hour = df['hour'].mode()[0]

    print('\n\nThe most common start hour is\n')
    print(":-")
    print(popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    d=df.groupby('Start Station')['Start Station'].count()
    d1=d.sort_values(ascending=False)
    print('The most popular Start Station is:- {}'.format(d1.index[0]))
    print('\n\n')


    # display most commonly used end station
    e=df.groupby('End Station')['End Station'].count()
    e1=e.sort_values(ascending=False)
    print('The most popular End staion is:- {}'.format(e1.index[0]))
    print('\n\n')


    # display most frequent combination of start station and end station trip
    f=df.groupby(['Start Station','End Station'])['Start Station'].count()
    f1=f.sort_values(ascending=False)
    print('The most frequent combination of start station and end station is:- {} and {}'.format(f1.index[0][0],f1.index[0][1]))
    print('\n\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    t1=df['Trip Duration'].sum()
    t2=df['Trip Duration'].mean()
    mi , sec=divmod(t1,60)
    hou , mi=divmod(mi,60)
    date,hou=divmod(hou,24)
    year,date=divmod(date,365)
    print(" the total trip duration is :- {} years {}days {}hours {}minutes {}seconds".format(year,date,hou,mi,sec))
    print('\n\n\n')
        # display mean travel time
    mi,sec=divmod(t2,60)
    hou, mi=divmod(mi,60)
    date,hou=divmod(hou,24)
    year,date=divmod(date,365)
    print(" the avaerage trip duration is :- {} years {}days {}hours {}minutes {}seconds".format(year,date,hou,mi,sec))
    print('\n\n\n')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The counts of user types is:\n')
    print(user_types)
    print('\n\n')




    # Display counts of gender
    if 'Gender' in df.columns:

        gender_count=df['Gender'].value_counts()
        print('The counts of gender is:\n')
        print(gender_count)
        print('\n\n')
    else:
        print("No gender values present\n")

    # Display earliest, most recent, and most common year of birth
    dobearliest=int(df['Birth Year'].min())
    print("The earliest birth year is : {}\n".format(dobearliest))
    dobrecent=int(df['Birth Year'].max())
    print('The most recent birth year is : {}\n'.format(dobrecent))
    dobcommon=int(df['Birth Year'].mode()[0])
    print("the most common birth year is : {}\n".format(dobcommon))
    print('\n\n')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df,df1 = load_data(city, month, day)
        i=0
        print("Do you want to look at first 5 rows of the dataset\n")
        print("Yes[Y] or No[N]\n\n")
        dic=input().lower()
        a1=0
        b1=5
        if dic =='n':
        else:
            while i<1:
                print(df1.iloc[a1:b1])
                print('\n\n')
                print("Do you want to print next 5 rows of dataset again\n")
                print("Yes[Y] or No[N]\n")
                dic2=input().lower()
                if dic2 =='n':
                    i=1
                else:
                    a1=b1
                    b1+=5
                    i=0







        time_stats(df1)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
