config() {
  NEW="$1"
  OLD="$(dirname $NEW)/$(basename $NEW .new)"
  # If there's no config file by that name, mv it over:
  if [ ! -r $OLD ]; then
    mv $NEW $OLD
  elif [ "$(cat $OLD | md5sum)" = "$(cat $NEW | md5sum)" ]; then
    # toss the redundant copy
    rm $NEW
  fi
  # Otherwise, we leave the .new copy for the admin to consider...
}

config usr/share/icons/WhiteSur-dark/index.theme.new
config usr/share/icons/WhiteSur-green-dark/index.theme.new
config usr/share/icons/WhiteSur-green-light/index.theme.new
config usr/share/icons/WhiteSur-green/index.theme.new
config usr/share/icons/WhiteSur-grey-dark/index.theme.new
config usr/share/icons/WhiteSur-grey-light/index.theme.new
config usr/share/icons/WhiteSur-grey/index.theme.new
config usr/share/icons/WhiteSur-light/index.theme.new
config usr/share/icons/WhiteSur-nord-dark/index.theme.new
config usr/share/icons/WhiteSur-nord-light/index.theme.new
config usr/share/icons/WhiteSur-nord/index.theme.new
config usr/share/icons/WhiteSur-orange-dark/index.theme.new
config usr/share/icons/WhiteSur-orange-light/index.theme.new
config usr/share/icons/WhiteSur-orange/index.theme.new
config usr/share/icons/WhiteSur-pink-dark/index.theme.new
config usr/share/icons/WhiteSur-pink-light/index.theme.new
config usr/share/icons/WhiteSur-pink/index.theme.new
config usr/share/icons/WhiteSur-purple-dark/index.theme.new
config usr/share/icons/WhiteSur-purple-light/index.theme.new
config usr/share/icons/WhiteSur-purple/index.theme.new
config usr/share/icons/WhiteSur-red-dark/index.theme.new
config usr/share/icons/WhiteSur-red-light/index.theme.new
config usr/share/icons/WhiteSur-red/index.theme.new
config usr/share/icons/WhiteSur-yellow-dark/index.theme.new
config usr/share/icons/WhiteSur-yellow-light/index.theme.new
config usr/share/icons/WhiteSur-yellow/index.theme.new
config usr/share/icons/WhiteSur/index.theme.new



