{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "2b68e907-9a8c-4650-bdda-f545cae88eba",
   "metadata": {},
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "import requests\n",
    "import re\n",
    "from csv import writer\n",
    "import time\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "520ccdab-37bc-419b-9aa2-2338df65abc1",
   "metadata": {},
   "source": [
    "Fetch company information"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "59e4e81a-6fc0-42d7-a317-0e399581d36a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "580\n"
     ]
    }
   ],
   "source": [
    "company_review=[]\n",
    "\n",
    "def get_company_review(tag,page):\n",
    "    #Get URL and Setup BeautifulSoup\n",
    "    url= f'https://www.trustpilot.com/review/www.{tag}.com?page={page}'\n",
    "    page=requests.get(url)\n",
    "    soup= BeautifulSoup(page.content,'html.parser')\n",
    "    companies=soup.find_all('section',class_='styles_reviewContentwrapper__zH_9M')\n",
    "    \n",
    "    #Create dictionary for review:\n",
    "    for company in companies:\n",
    "        #CompanyName\n",
    "        companyName=tag\n",
    "        #DatePublished\n",
    "        datePublished=company.find('div',class_=\"typography_typography__QgicV typography_bodysmall__irytL typography_color-gray-6__TogX2 typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3 styles_datesWrapper__RCEKH\").time.attrs['datetime']\n",
    "        #reviewBody\n",
    "        reviewBody=company.find('p',class_='typography_typography__QgicV typography_body__9UBeQ typography_color-black__5LYEn typography_weight-regular__TWEnf typography_fontstyle-normal__kHyN3')\n",
    "        if reviewBody is None: #Some review does not have reviewbody\n",
    "            reviewBody = 'Empty'\n",
    "        else:\n",
    "            reviewBody=reviewBody.text\n",
    "        #RatingValue\n",
    "        ratingValue=company.find('div',class_='styles_reviewHeader__iU9Px').attrs['data-service-review-rating']\n",
    "        #Dictionary\n",
    "        review_dir={\n",
    "            'companyName':companyName,\n",
    "            'datePublished':datePublished,\n",
    "            'reviewBody':reviewBody,\n",
    "            'ratingValue':ratingValue        \n",
    "        }\n",
    "        company_review.append(review_dir)\n",
    "    return\n",
    "\n",
    "#Scrap number of pages:\n",
    "for x in range(0,30):\n",
    "    get_company_review('facebook',x)\n",
    "print(len(company_review))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "70dd5652-4115-4bef-800a-6857d116624c",
   "metadata": {},
   "source": [
    "Save to csv file"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "2e2dad66-d695-4611-af52-65365c78a963",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>companyName</th>\n",
       "      <th>datePublished</th>\n",
       "      <th>reviewBody</th>\n",
       "      <th>ratingValue</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2022-05-19T21:21:13.000Z</td>\n",
       "      <td>Empty</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2022-05-19T19:23:03.000Z</td>\n",
       "      <td>I am not setting Facebook down because as far ...</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2022-05-19T17:04:39.000Z</td>\n",
       "      <td>I was a Facebook user for over 10 years and af...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2022-05-19T13:10:53.000Z</td>\n",
       "      <td>Facebook customer service is TERRIBLE!I am sho...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2022-05-18T20:56:36.000Z</td>\n",
       "      <td>Facebook is one of the most racist platforms o...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>575</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2021-10-26T11:04:50.000Z</td>\n",
       "      <td>Facebook suspended my profile for advertising ...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>576</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2021-10-26T01:49:51.000Z</td>\n",
       "      <td>This is the worst place to be Facebook is full...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>577</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2021-10-25T21:28:28.000Z</td>\n",
       "      <td>Can't have an opinion that is fact based and b...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>578</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2021-10-25T13:26:33.000Z</td>\n",
       "      <td>Where do I start? Everything about this compan...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>579</th>\n",
       "      <td>facebook</td>\n",
       "      <td>2021-10-25T12:06:41.000Z</td>\n",
       "      <td>The latest update about in stream Ads is too m...</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>580 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "    companyName             datePublished  \\\n",
       "0      facebook  2022-05-19T21:21:13.000Z   \n",
       "1      facebook  2022-05-19T19:23:03.000Z   \n",
       "2      facebook  2022-05-19T17:04:39.000Z   \n",
       "3      facebook  2022-05-19T13:10:53.000Z   \n",
       "4      facebook  2022-05-18T20:56:36.000Z   \n",
       "..          ...                       ...   \n",
       "575    facebook  2021-10-26T11:04:50.000Z   \n",
       "576    facebook  2021-10-26T01:49:51.000Z   \n",
       "577    facebook  2021-10-25T21:28:28.000Z   \n",
       "578    facebook  2021-10-25T13:26:33.000Z   \n",
       "579    facebook  2021-10-25T12:06:41.000Z   \n",
       "\n",
       "                                            reviewBody ratingValue  \n",
       "0                                                Empty           1  \n",
       "1    I am not setting Facebook down because as far ...           3  \n",
       "2    I was a Facebook user for over 10 years and af...           1  \n",
       "3    Facebook customer service is TERRIBLE!I am sho...           1  \n",
       "4    Facebook is one of the most racist platforms o...           1  \n",
       "..                                                 ...         ...  \n",
       "575  Facebook suspended my profile for advertising ...           1  \n",
       "576  This is the worst place to be Facebook is full...           1  \n",
       "577  Can't have an opinion that is fact based and b...           1  \n",
       "578  Where do I start? Everything about this compan...           1  \n",
       "579  The latest update about in stream Ads is too m...           1  \n",
       "\n",
       "[580 rows x 4 columns]"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df= pd.DataFrame(company_review)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "fd1be669-88eb-4ec8-8bfd-a20d2fc76fb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_csv('company_review.csv',index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a543d9a-8478-4433-9ba4-2154b3171571",
   "metadata": {},
   "source": [
    "Function to save in CSV(Use for later)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e2a049fd-c884-4b8d-a31f-fb7012b0c928",
   "metadata": {},
   "outputs": [],
   "source": [
    "def write_to_csv(header):\n",
    "    try:\n",
    "        with open('company_review.csv','a',encoding='utf-8',newline='') as f:\n",
    "            thewriter=writer(f)\n",
    "            thewriter.writerow(header)\n",
    "    except:\n",
    "        return False"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "19700154-edad-43ca-bb3d-ee6c150657a2",
   "metadata": {},
   "source": [
    "Reference:\n",
    "\n",
    "How Web Scrape Multiple Pages with ONE Function with Python:\n",
    "https://www.youtube.com/watch?v=m-koIYWCaIo\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  },
  "toc-autonumbering": true,
  "toc-showmarkdowntxt": true
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
