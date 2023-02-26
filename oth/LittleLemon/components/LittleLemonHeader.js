import { View, Text, StyleSheet } from 'react-native';

export default function LittleLemonHeader() {
  return (
    <View style={style.box}>
      <Text
        style={style.text}>
        Little Lemon
      </Text>
    </View>
  );
}

const style = StyleSheet.create({
  box : {
    flex: 0.1,
    backgroundColor: '#EE9972'
  },
  text : {
    padding: 20,
    fontSize: 30,
    color: 'black',
    textAlign: 'center',
  }
})