import React from "react";
import { View, Text, ScrollView, StyleSheet, FlatList } from 'react-native';
/*
const menuItemsToDisplay = [
    'Hummus \n Moutabal \n Falafel \n Marinated Olives \n Kofta \n Eggplant Salad \n Lentil Burger \n Smoked Salmon \n Kofta Burger \n Turkish Kebab \n Fries \n Buttered Rice \n Bread Sticks \n Pita Pocket \n Lentil Soup \n Greek Salad \n Rice Pilaf \n Baklava \n Tartufo \n Tiramisu \n Panna Cotta',
];
*/
const menuItemsToDisplay = [
    { name: 'Hummus', price: '$5.00', id: '1A' },
    { name: 'Moutabal', price: '$5.00', id: '2B' },
    { name: 'Falafel', price: '$7.50', id: '3C' },
    { name: 'Marinated Olives', price: '$5.00', id: '4D' },
    { name: 'Kofta', price: '$5.00', id: '5E' },
    { name: 'Eggplant Salad', price: '$8.50', id: '6F' },
    { name: 'Lentil Burger', price: '$10.00', id: '7G' },
    { name: 'Smoked Salmon', price: '$14.00', id: '8H' },
    { name: 'Kofta Burger', price: '$11.00', id: '9I' },
    { name: 'Turkish Kebab', price: '$15.50', id: '10J' },
    { name: 'Fries', price: '$3.00', id: '11K' },
    { name: 'Buttered Rice', price: '$3.00', id: '12L' },
    { name: 'Bread Sticks', price: '$3.00', id: '13M' },
    { name: 'Pita Pocket', price: '$3.00', id: '14N' },
    { name: 'Lentil Soup', price: '$3.75', id: '15O' },
    { name: 'Greek Salad', price: '$6.00', id: '16Q' },
    { name: 'Rice Pilaf', price: '$4.00', id: '17R' },
    { name: 'Baklava', price: '$3.00', id: '18S' },
    { name: 'Tartufo', price: '$3.00', id: '19T' },
    { name: 'Tiramisu', price: '$5.00', id: '20U' },
    { name: 'Panna Cotta', price: '$5.00', id: '21V' },
  ];

const MenuItems = () => {
    const renderItem = ({ item }) => <Item name={item.name} price={item.price} />;

    const Item = ({ name, price }) => (
        <View style={menuStyles.innerContainer}>
          <Text style={menuStyles.itemTextLeft}>{name}</Text>
          <Text style={menuStyles.itemTextRight}>{price}</Text>
        </View>
      );

    return (
        <View style={menuStyles.container}>
        <FlatList data={menuItemsToDisplay} keyExtractor={item => item.id} renderItem={renderItem} />
        </View>
    );
};

menuStyles = StyleSheet.create({
    container: {
        flex: 0.85
      },
      innerContainer: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center', 
        paddingHorizontal: 40,
        paddingVertical: 20,
        backgroundColor: '#333333',
      },
      headerText: {
        color: 'white',
        fontSize: 40,
        flexWrap: 'wrap',
        textAlign: 'center',
      },
      itemTextLeft: {
        color: '#F4CE14',
        fontSize: 20,
      },
      itemTextRight: {
        color: '#F4CE14',
        fontSize: 20,
    },
})
{/* Stick with convection and put commas at end */}

export default MenuItems;

/*
        <View style={{flex : 0.75}}>
            /*
            <FlatList data={menuItemsToDisplay} >

            </FlatList>
            */
            /*
            <ScrollView
            indicatorStyle={"White"}
            style={{
                paddingHorizontal: 40,
                paddingVertical: 40,
                backgroundColor: "black"
            }}>
            <Text style={{ color: 'white', fontSize: 40, flexWrap: 'wrap' }}>
                View Menu
            </Text>
            <Text style={{ color: '#F4CE14', fontSize: 36 }}>
              {menuItemsToDisplay[0]}
            </Text>
            </ScrollView>
            </View>
*/