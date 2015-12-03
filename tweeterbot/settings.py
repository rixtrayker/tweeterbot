"""
Django settings for tweeterbot project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1z77sl5efyy(y^s4lroft$ge*k78_zz($^b2^50f#ym5+kmu@t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'tweeterapp',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tweeterbot.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'tweeterbot.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'


SOCIAL_AUTH_TWITTER_KEY='Pmn1PSUEjRPBQNj5N2NlqgZF0' #aPPjGSzKevzuAmAbSCxkOWWm1'
SOCIAL_AUTH_TWITTER_SECRET='rKgejho6yM4mMQmovpFMFE8bAfb5Meb9TwE2qBBhpyjlGfptgI' #0NUD8IdfJVl7vuVk2BoLD1q5L6YledVmnDrPZA81ztqXTVkktt'

AUTHENTICATION_BACKENDS = (
    #'social.backends.amazon.AmazonOAuth2',
    #'social.backends.angel.AngelOAuth2',
    #'social.backends.aol.AOLOpenId',
    #'social.backends.appsfuel.AppsfuelOAuth2',
    #'social.backends.beats.BeatsOAuth2',
    #'social.backends.behance.BehanceOAuth2',
    #'social.backends.belgiumeid.BelgiumEIDOpenId',
    #'social.backends.bitbucket.BitbucketOAuth',
    #'social.backends.box.BoxOAuth2',
    #'social.backends.clef.ClefOAuth2',
    #'social.backends.coinbase.CoinbaseOAuth2',
    #'social.backends.coursera.CourseraOAuth2',
    #'social.backends.dailymotion.DailymotionOAuth2',
    #'social.backends.disqus.DisqusOAuth2',
    #'social.backends.douban.DoubanOAuth2',
    #'social.backends.dropbox.DropboxOAuth',
    #'social.backends.dropbox.DropboxOAuth2',
    #'social.backends.eveonline.EVEOnlineOAuth2',
    #'social.backends.evernote.EvernoteSandboxOAuth',
    #'social.backends.facebook.FacebookAppOAuth2',
    #'social.backends.facebook.FacebookOAuth2',
    #'social.backends.fedora.FedoraOpenId',
    #'social.backends.fitbit.FitbitOAuth',
    #'social.backends.flickr.FlickrOAuth',
    #'social.backends.foursquare.FoursquareOAuth2',
    #'social.backends.github.GithubOAuth2',
    #'social.backends.google.GoogleOAuth',
    #'social.backends.google.GoogleOAuth2',
    #'social.backends.google.GoogleOpenId',
    #'social.backends.google.GooglePlusAuth',
    #'social.backends.google.GoogleOpenIdConnect',
    #'social.backends.instagram.InstagramOAuth2',
    #'social.backends.jawbone.JawboneOAuth2',
    #'social.backends.kakao.KakaoOAuth2',
    #'social.backends.linkedin.LinkedinOAuth',
    #'social.backends.linkedin.LinkedinOAuth2',
    #'social.backends.live.LiveOAuth2',
    #'social.backends.livejournal.LiveJournalOpenId',
    #'social.backends.mailru.MailruOAuth2',
    #'social.backends.mendeley.MendeleyOAuth',
    #'social.backends.mendeley.MendeleyOAuth2',
    #'social.backends.mineid.MineIDOAuth2',
    #'social.backends.mixcloud.MixcloudOAuth2',
    #'social.backends.nationbuilder.NationBuilderOAuth2',
    #'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
    #'social.backends.open_id.OpenIdAuth',
    #'social.backends.openstreetmap.OpenStreetMapOAuth',
    #'social.backends.persona.PersonaAuth',
    #'social.backends.podio.PodioOAuth2',
    #'social.backends.rdio.RdioOAuth1',
    #'social.backends.rdio.RdioOAuth2',
    #'social.backends.readability.ReadabilityOAuth',
    #'social.backends.reddit.RedditOAuth2',
    #'social.backends.runkeeper.RunKeeperOAuth2',
    #'social.backends.skyrock.SkyrockOAuth',
    #'social.backends.soundcloud.SoundcloudOAuth2',
    #'social.backends.spotify.SpotifyOAuth2',
    #'social.backends.stackoverflow.StackoverflowOAuth2',
    #'social.backends.steam.SteamOpenId',
    #'social.backends.stocktwits.StocktwitsOAuth2',
    #'social.backends.stripe.StripeOAuth2',
    #'social.backends.suse.OpenSUSEOpenId',
    #'social.backends.thisismyjam.ThisIsMyJamOAuth1',
    #'social.backends.trello.TrelloOAuth',
    #'social.backends.tripit.TripItOAuth',
    #'social.backends.tumblr.TumblrOAuth',
    #'social.backends.twilio.TwilioAuth',
    'social.backends.twitter.TwitterOAuth',
    #'social.backends.vk.VKOAuth2',
    #'social.backends.weibo.WeiboOAuth2',
    #'social.backends.wunderlist.WunderlistOAuth2',
    #'social.backends.xing.XingOAuth',
    #'social.backends.yahoo.YahooOAuth',
    #'social.backends.yahoo.YahooOpenId',
    #'social.backends.yammer.YammerOAuth2',
    #'social.backends.yandex.YandexOAuth2',
    #'social.backends.vimeo.VimeoOAuth1',
    #'social.backends.lastfm.LastFmAuth',
    #'social.backends.moves.MovesOAuth2',
    #'social.backends.vend.VendOAuth2',
    #'social.backends.email.EmailAuth',
    #'social.backends.username.UsernameAuth',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_USER_MODEL = 'auth.User'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/done/'
URL_PATH = ''
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]
# SOCIAL_AUTH_EMAIL_FORM_URL = '/signup-email'
SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'example.app.mail.send_validation'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
# SOCIAL_AUTH_USERNAME_FORM_URL = '/signup-username'
SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'

#SOCIAL_AUTH_PIPELINE = (
#    'social.pipeline.social_auth.social_details',
#    'social.pipeline.social_auth.social_uid',
#    'social.pipeline.social_auth.auth_allowed',
#    'social.pipeline.social_auth.social_user',
#    'social.pipeline.user.get_username',
#    'example.app.pipeline.require_email',
#    'social.pipeline.mail.mail_validation',
#    'social.pipeline.user.create_user',
#    'social.pipeline.social_auth.associate_user',
#    'social.pipeline.debug.debug',
#    'social.pipeline.social_auth.load_extra_data',
#    'social.pipeline.user.user_details',
#    'social.pipeline.debug.debug'
#)
