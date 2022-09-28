# ------------------------------------------Step-1 --------------------------------------------------------------------------------
# Importing required libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------------------Step-2 --------------------------------------------------------------------------------
# Basic Page Configurations to to make GUI a little better
st.set_page_config(page_title="Hospitality Dashboard",
                  page_icon=":bar_chart:",
                  layout="wide"
                  )


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style> """, unsafe_allow_html=True)


# adding dark theme to the plt plots to match overall GUI
plt.style.use("dark_background")

st.sidebar.image("codebasics.png", use_column_width=True)

# Adding Header
st.markdown("<hr/>",unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>Atliq Grands Hotel's Hospitality Data Visualization</h1>", unsafe_allow_html=True)

# Adding credential sidebar
st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Project challenge from Code Basics</h1>", unsafe_allow_html=True)

st.sidebar.markdown("<hr/>",unsafe_allow_html=True)
# Adding Side bar along with width and height field for some plots
st.sidebar.markdown(
    "<h5 style='text-align: left; color: orange;'>Use These sliders to change height and width of 2nd and last plots</h5>", unsafe_allow_html=True)
width = st.sidebar.slider("Width", min_value=6, max_value=20, value=10)
height = st.sidebar.slider("Height", min_value=1, max_value=10, value=3)

# ------------------------------------------Step-3 --------------------------------------------------------------------------------
# Loading Dataframes cache
@st.cache
def load_date_data(path):
    df1 = pd.read_csv(path)
    return df1
def load_hotels_data(path):
    df2 = pd.read_csv(path)
    return df2
def load_rooms_data(path):
    df3= pd.read_csv(path)
    return df3
def load_fact_aggregated_bookings(path):
    df4 =pd.read_csv(path)
    return df4
def load_fact_bookings(path):
    df5 = pd.read_csv(path)
    return df5

# Loading datas and Dataframes of datasets
data1 = load_date_data("Dataset/dim_date.csv")
data2 = load_hotels_data("Dataset/dim_hotels.csv")
data3 = load_rooms_data("Dataset/dim_rooms.csv")
data4 = load_fact_aggregated_bookings("Dataset/fact_aggregated_bookings.csv")
data5 = load_fact_bookings("Dataset/fact_bookings.csv")

st.markdown("<hr/>",unsafe_allow_html=True)

# ------------------------------------------Step-4 --------------------------------------------------------------------------------
# 4 Some Basic information about data
# intial step 4coloumns

c0, c1,c2,c3 = st.columns(4)  # creating 4 containers for metrics
#c0
with c0:
    st.markdown("<h3 style='text-align: center;'>Total Revenue</h3>", unsafe_allow_html=True)
    c0 = data5["revenue_realized"].sum()
    st.markdown(f"<h3 style='text-align: center; color:red; '>{c0} ₹</h3> ",unsafe_allow_html=True)

#c1
with c1:
    st.markdown("<h3 style='text-align: center;'>Total Bookings</h3>", unsafe_allow_html=True)
    c1 = len(data5["booking_id"])
    st.markdown(f"<h3 style='text-align: center; color:red;'>{c1}</h3> ",unsafe_allow_html=True)

#c2
with c2:
    st.markdown("<h3 style='text-align: center;'>Average rating</h3>", unsafe_allow_html=True)
    c2 = data5["ratings_given"].dropna().astype("float64").mean()
    star_Rating = "⭐" * int(round(c2,0))
    st.markdown(f"<h3 style='text-align: center; color:red;'>{int(round(c2,0))}{star_Rating}</h3> ",unsafe_allow_html=True)

#c3
with c3:
    st.markdown("<h3 style='text-align: center;'>Total Capacity</h3>", unsafe_allow_html=True)
    c3 = data4["capacity"].sum()
    st.markdown(f"<h3 style='text-align: center; color:red;'>{c3}</h3> ",unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)

c4, c5,c6,c7 = st.columns(4) # adding other 4 metrices to containors
#c4
with c4:
    st.markdown("<h3 style='text-align: center;'>Total Successful Bookings</h3>", unsafe_allow_html=True)
    c4 = data4["successful_bookings"].sum() 
    st.markdown(f"<h3 style='text-align: center; color:red;'>{c4}</h3> ",unsafe_allow_html=True)

#c5
with c5:
    st.markdown("<h3 style='text-align: center;'>Occupancy</h3>", unsafe_allow_html=True)
    # round(100* c4 = Total_successful_bookings /  c3 = Total_Capacity,2)
    c5 = round(100*c4 / c3,2) 
    st.markdown(f"<h3 style='text-align: center; color:red;'>{c5} %</h3> ",unsafe_allow_html=True)

#c6
with c6:
    st.markdown("<h3 style='text-align: center;'>Total Cancelled Bookings</h3>", unsafe_allow_html=True)
    c6 = (data5["booking_status"] == "Cancelled").sum()
    st.markdown(f"<h3 style='text-align: center; color:red;'>{c6}</h3> ",unsafe_allow_html=True)    

#c7
with c7:
    st.markdown("<h3 style='text-align: center;'>Cancellation Rate</h3>", unsafe_allow_html=True)
    #round(100*c6 = Total_Cancelled_Bookings/c1 = Total_Bookings,2 )
    c7 = round(100*c6/c1,2 ) 
    st.markdown(f"<h3 style='text-align: center; color:red;'>{c7}</h3> ",unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)

st.markdown("<h2 style='text-align: center;'>Data Visualization</h2>", unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)

# ------------------------------------------Step-5 --------------------------------------------------------------------------------
# 5 Total data data distribution accornding to the selection-----
# graph1
# bprcpirg = Booking Platform , Room Category, Property ID, Ratings given
bprcpirg = st.selectbox(" Select One Of The Following : Booking Platform , Room Category, Property ID, Ratings given",["booking_platform", "room_category","property_id", "ratings_given","revenue_realized"])
st.subheader(bprcpirg + " : wise data distribution ")
st.bar_chart(data5[bprcpirg].value_counts(),height=300, use_container_width=True)

st.markdown("<hr/>",unsafe_allow_html=True)
# graph2
# cpn = City or Property_name"
cpn = st.selectbox("Select One Of The Following : City or Property_name",["city", "property_name"])
st.markdown(cpn + " : wise data distribution ")
st.bar_chart(data2[cpn].value_counts(), height=300, use_container_width=True)

st.markdown("<hr/>",unsafe_allow_html=True)

# ------------------------------------------Step-6 --------------------------------------------------------------------------------
# 6 Revenue plot in millions based on booking platform
fig, ax = plt.subplots(figsize=(width, height))
st.markdown("<h1 style='text-align: center;'>Revenue History</h1>", unsafe_allow_html=True)

op1 = st.multiselect("Select Revenue",["revenue_generated","revenue_realized"], default =["revenue_realized","revenue_generated"])
group1 = data5.groupby('booking_platform').sum()
ax.plot(group1[op1], label=op1)
ax.set_xlabel("Booking Platform")
ax.set_ylabel("Revenue in millions")
ax.legend()
st.pyplot(fig)

st.markdown("<hr/>",unsafe_allow_html=True)

# ------------------------------------------Step-7 --------------------------------------------------------------------------------
# 7 pie chart of various data
left, right = st.columns(2) # creating two container/columns for piecharts

# 7.1
left.subheader("Revenue_generated & Revenue_realized")
lst = []
plt.figure(2).figsize=(5,5) #assigning figure number to plot for using later

data_new = data5[[ "revenue_generated","revenue_realized"]]
for i in data_new.columns[:]:
    lst.append(sum(data_new[i]))

mylabels = data_new.columns[:]
plt.pie(lst, labels = mylabels,shadow=True, autopct='%1.1f%%',colors=["green","blue"])
plt.legend()
plt.tight_layout()
left.pyplot(plt.figure(2))

# 7.2 
right.subheader("Succcessful bookings and Total capacity")
lst = []
plt.figure(3).figsize=(5,5) #assigning figure number to plot for using later

data_new2 = data4[[ "successful_bookings","capacity"]]
for i in data_new2.columns[:]:
    lst.append(sum(data_new2[i]))

mylabels = data_new2.columns[:]
plt.pie(lst, labels = mylabels,shadow=True, autopct='%1.1f%%',colors=["green","blue"])
plt.legend()
plt.tight_layout()
right.pyplot(plt.figure(3))

st.markdown("<hr/>",unsafe_allow_html=True)

#7.3
new_c0,new_c1 = st.columns(2)
new_c0.subheader("Revenue based on booking platforms")
plt.figure(4).figsize=(5,5)
group1 = data5.groupby("booking_platform").sum()
mylabels = data5["booking_platform"].unique()
plt.pie(group1["revenue_realized"], labels=mylabels, shadow=True, autopct='%1.1f%%',colors=["purple","red","magenta","blue","green","violet","indigo"])
plt.legend(loc='center left')
plt.tight_layout()
new_c0.pyplot(plt.figure(4))

#7.4
new_c1.subheader("room category based on revenue")
plt.figure(5).figsize=(5,5)
group1 = data5.groupby("room_category").sum()
mylabels = data5["room_category"].unique()
plt.pie(group1["revenue_realized"], labels=mylabels,shadow=True, autopct='%1.1f%%',colors=["blue","green","violet","orange"])
plt.legend()
plt.tight_layout()
new_c1.pyplot(plt.figure(5))

st.markdown("<hr/>",unsafe_allow_html=True)

# ------------------------------------------Step-8 --------------------------------------------------------------------------------
# 8 booking platform wise Average revenue generated, revenue realized
st.markdown("<h1 style='text-align: center;'>booking platform wise Average revenue</h1>", unsafe_allow_html=True)
data_new3 = data5[[ "revenue_generated","revenue_realized","booking_platform"]]
cols = list(data_new3.columns[:])
op3 = st.multiselect(
    "Select Revenue Category", ["revenue_generated","revenue_realized"], default=["revenue_realized","revenue_generated"])
# Grouping data by Genre by using method of mean
result = data_new3.groupby(['booking_platform']).mean()
st.bar_chart(result[op3], height=350, use_container_width=True)

st.markdown("<hr/>",unsafe_allow_html=True)


# ------------------------------------------Step-9 --------------------------------------------------------------------------------
#9 Top 10 revenue_realized by booking platform

st.markdown("<h1 style='text-align: center;'>Top 10 Revenues Realized and Generated</h1>", unsafe_allow_html=True)
left,right = st.columns(2)

platf = sorted(data5["booking_platform"].unique())
p = left.selectbox("Select platform", platf)
left.subheader("Top 10 Revenues realized by booking platforms")

# making new datafreame with booking_platform = to required platform
df = data5.query("booking_platform == @p")

# sorting the dataframe in decending order on revenue_realized

df = df.sort_values(by=["revenue_realized"], ascending=False)
df = df.iloc[:11]
df = df[["booking_status","revenue_realized"]]
left.table(df)

#9.2
generated = sorted(data5["booking_platform"].unique())
g  = right.selectbox("Select platform", generated, index=6)
right.subheader("Top 10 Revenue generated by booking platform")
# making new datafreame with booking_platform = to required platform
df01 = data5.query("booking_platform == @g")
# sorting the dataframe in decending order on revenue_generated
df01 = df01.sort_values(by=["revenue_generated"], ascending=False)
df01 = df01.iloc[:10]
df01 = df01[["booking_status", "revenue_generated"]]
right.table(df01)

st.markdown("<hr/>",unsafe_allow_html=True)


# ------------------------------------------Step-10 --------------------------------------------------------------------------------
# 10 Comparing Revenue data of  booking status and ratings given by booking platform
st.markdown("<h3 style='text-align: center;'>Comparing Revenue data of  booking status and ratings given by booking platform</h3>", unsafe_allow_html=True)
st.markdown("<hr/>",unsafe_allow_html=True)
status = sorted(data5["booking_status"].unique())
a = data5["ratings_given"].dropna()
ratings = sorted(a.unique())
left,right = st.columns(2)
# Selecting two booking status and ratings
c01 = left.selectbox("Select the booking status", status, index = 2)
c02 = right.selectbox("Select the Ratings given", ratings, index=4)

# creating dataframe of 2  selected booking status and ratings given
df1 = data5.query("booking_status== @c01")
df2 = data5.query("ratings_given == @c02")

# grouping  the data by booking platform
group2 = df1.groupby("booking_platform").sum()
group3 = df2.groupby("booking_platform").sum()

# Plotting
fig3, ax = plt.subplots(figsize=(width,height))
ax.bar(group2.index,group2["revenue_realized"],label=c01,color="Red")
ax.bar(group3.index,group3["revenue_realized"],label=c02, color="orange")
ax.set_xlabel("booking platform")
ax.set_ylabel("revenue realized in millions")
ax.legend()
st.pyplot(fig3)



st.markdown("<hr/>",unsafe_allow_html=True)


# ------------------------------------------Step-11 --------------------------------------------------------------------------------
# 11 Checkbox to show datasets
st.markdown("<h3 style='text-align: center;'>Datasets</h3>", unsafe_allow_html=True)

st.markdown("<hr/>",unsafe_allow_html=True)
if st.checkbox('Show dim Date Data'):
    st.write(data1)

if st.checkbox('Show dim Hotel Data'):
    st.write(data2)

if st.checkbox('Show dim rooms Data'):
    st.write(data3)

if st.checkbox('Show fact_aggregated_bookings Data'):
    st.write(data4)

if st.checkbox('Show fact_bookings Data'):
    st.write(data5)
st.markdown("<hr/>",unsafe_allow_html=True)


# ------------------------------------------Step-12 --------------------------------------------------------------------------------
# Adding credential 
st.markdown("<h5 style='text-align: center;'> MADE BY SHRIHITH.A </h5>", unsafe_allow_html=True)
# st.markdown("<h5 style='text-align: right;'>Made by Shrihith A</h5>", unsafe_allow_html=True)






