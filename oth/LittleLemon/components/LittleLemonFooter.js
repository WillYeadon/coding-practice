import { View, Text, StyleSheet } from 'react-native';

export default function LittleLemonFooter() {
  return (
    <View style={style.oldView}>
      <Text
        style={style.text}>
        All rights reserved by Little Lemon, 2022
      </Text>
    </View>
  );
}

const style = StyleSheet.create({
  oldView : { flex: 1,
    backgroundColor: '#EE9972',
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0
    },
  text : {
    padding: 10,
    color: 'black',
    textAlign: 'center',
    fontSize: 15
    }
})