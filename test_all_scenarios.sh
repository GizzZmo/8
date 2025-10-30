#!/bin/bash
# Comprehensive test script for OSI simulation

echo "======================================"
echo "OSI Blockchain Simulation Test Suite"
echo "======================================"
echo ""

cd osi_blockchain_simulation

echo "Test 1: Basic Text Transmission"
echo "--------------------------------"
python main_simulation.py --data "Test Message" 2>&1 | grep -E "(Original Data|Final Data Received|COMPLETE)"
echo ""

echo "Test 2: Encrypted Transmission"
echo "-------------------------------"
python main_simulation.py --data "Encrypted" --encrypt 2>&1 | grep -E "(Encrypted Payload|Decrypting|Original Data|Final Data)"
echo ""

echo "Test 3: Signed Transmission"
echo "---------------------------"
python main_simulation.py --data "Signed" --sign 2>&1 | grep -E "(Signed Payload|Signature verified|Final Data)"
echo ""

echo "Test 4: Blockchain Transaction"
echo "-------------------------------"
python main_simulation.py --blockchain 2>&1 | grep -E "(sender|receiver|amount|Final Data)"
echo ""

echo "Test 5: Combined (Encrypt + Sign)"
echo "----------------------------------"
python main_simulation.py --data "Secret" --encrypt --sign 2>&1 | grep -E "(Encrypted|Signed|Decrypting|verified|Final)"
echo ""

echo "======================================"
echo "All Tests Complete!"
echo "======================================"
