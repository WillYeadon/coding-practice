import { View, Text, ScrollView, StyleSheet } from 'react-native';

export default function WelcomeScreen() {
  return (
    <View style={{ flex: 1 }}>
      <ScrollView
        indicatorStyle={"White"}
        style={style.scroll}>
      <Text style={style.title}>
        Welcome to Little Lemon
      </Text>
      <Text style={style.body}>
      Little Lemon is a charming neighborhood bistro that serves simple food and classic cocktails in a lively but casual environment. We would love to hear more about your experience with us!
      </Text>
      </ScrollView>
    </View>
  );
}

const style = StyleSheet.create({
  scroll: {
    flex: 1,
    paddingHorizontal: 10,
    paddingVertical: 10,
    backgroundColor: '#333333'
  },
  title: {
    textAlign: 'center',
    padding: 30,
    fontSize: 50,
    color: '#EDEFEE'
  },
  body: {
    textAlign: 'center',
    padding: 50,
    fontSize: 35,
    color: '#EDEFEE'
  }
})