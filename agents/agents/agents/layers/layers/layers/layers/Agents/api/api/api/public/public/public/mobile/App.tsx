import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, TextInput, Button } from 'react-native';
import { useState } from 'react';

export default function App() {
  const [invocation, setInvocation] = useState('');

  const sendInvocation = () => {
    // Fetch to backend /invoke
    console.log('Invocation sent:', invocation);
  };

  return (
    <View style={styles.container}>
      <Text>Nia LeSane CEO</Text>
      <TextInput
        style={styles.input}
        placeholder="Speak to Nia..."
        value= {invocation}
        onChangeText={setInvocation}
      />
      <Button title="Launch Ritual" onPress= {sendInvocation} />
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0a0a0a',
    alignItems: 'center',
    justifyContent: 'center',
  },
  input: {
    backgroundColor: '#1a1a1a',
    color: '#e0e0e0',
    width: '80%',
    padding: 15,
    margin: 20,
  },
});
