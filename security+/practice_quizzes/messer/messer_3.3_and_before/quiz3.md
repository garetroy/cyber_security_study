# CSRT Advanced Practice Quiz

**Score: 27/30**  
**Percentage: 90%**

---

1. **Which of the following is a key aspect of the Zero Trust model?**  
   - A) Implicit trust within the local network  
   - B) Trust-based access control  
   - C) Assume breach and verify every access request  
   - D) Trust based on user’s IP address  

   _Answered Correctly: C) Assume breach and verify every access request_  
   _Explanation:_ The Zero Trust model operates on the assumption that threats could be inside or outside the network and therefore verifies every access attempt, regardless of its source.

---

2. **What is the primary purpose of Security Information and Event Management (SIEM) correlation rules?**  
   - A) To encrypt event logs for secure storage  
   - B) To provide user access management  
   - C) To automate incident response actions  
   - D) To analyze and relate multiple security events for pattern detection  

   _Answered Correctly: D) To analyze and relate multiple security events for pattern detection_  
   _Explanation:_ SIEM correlation rules help identify patterns in security events that might indicate threats, enhancing threat detection capabilities.

---

3. **Which of the following best describes a compensating control in a risk management framework?**  
   - A) A temporary control used until a more effective one is implemented  
   - B) A control that reduces the impact of an attack  
   - C) A control that enhances an existing security measure  
   - D) A control that replaces all other security measures  

   _Answered Correctly: A) A temporary control used until a more effective one is implemented_  
   _Explanation:_ Compensating controls are alternative measures used when primary controls are not feasible, offering temporary risk mitigation until a more effective control can be implemented.

---

4. **In the context of digital certificates, what role does the Online Certificate Status Protocol (OCSP) play?**  
   - A) It generates digital signatures  
   - B) It revokes invalid certificates from the database  
   - C) It allows real-time verification of a certificate’s status  
   - D) It manages the key exchange process  

   _Answered Correctly: C) It allows real-time verification of a certificate’s status_  
   _Explanation:_ OCSP enables real-time checks of a certificate's validity, helping to ensure that expired or revoked certificates are not used.

---

5. **Which of the following is a key function of a Security Operations Center (SOC)?**  
   - A) Designing security architectures  
   - B) Conducting physical security patrols  
   - C) Continuous monitoring and analysis of security alerts  
   - D) Developing security policies and procedures  

   _Answered Correctly: C) Continuous monitoring and analysis of security alerts_  
   _Explanation:_ A SOC focuses on real-time monitoring, analysis, and response to security incidents, aiming to protect the organization’s infrastructure.

---

6. **What type of attack involves injecting malicious code into a website’s input fields to manipulate a database query?**  
   - A) Cross-Site Scripting (XSS)  
   - B) SQL Injection  
   - C) Command Injection  
   - D) LDAP Injection  

   _Answered Correctly: B) SQL Injection_  
   _Explanation:_ SQL injection involves manipulating a database query through input fields, potentially accessing or altering database content.

---

7. **Which of the following best describes a heuristic-based detection system in an IDS/IPS?**  
   - A) It relies on known attack signatures to detect threats.  
   - B) It uses anomaly detection by comparing current activity to a baseline.  
   - C) It learns and adapts to new threats over time.  
   - D) It performs static analysis of incoming traffic.  

   _Answered Correctly: B) It uses anomaly detection by comparing current activity to a baseline._  
   _Explanation:_ Heuristic-based detection involves comparing behaviors to a baseline to detect deviations that might indicate threats.

---

8. **In a Security Orchestration, Automation, and Response (SOAR) system, what is the main benefit of playbooks?**  
   - A) They provide encryption keys for secure communication.  
   - B) They automate repetitive security tasks and responses.  
   - C) They store user credentials securely.  
   - D) They analyze network traffic patterns for anomalies.  

   _Answered Correctly: B) They automate repetitive security tasks and responses._  
   _Explanation:_ Playbooks in a SOAR system automate incident response processes, reducing the need for manual intervention and speeding up response times.

---

9. **What does the term *mean time to detect (MTTD)* refer to in incident response?**  
   - A) The average time it takes to resolve an incident  
   - B) The average time it takes to detect a security breach  
   - C) The average time between detected incidents  
   - D) The time required to mitigate an incident after detection  

   _Answered Correctly: B) The average time it takes to detect a security breach_  
   _Explanation:_ MTTD measures how quickly an organization can identify that an incident has occurred.

---

10. **Which control is most effective at limiting lateral movement after a breach within a network?**  
    - A) Network segmentation  
    - B) User awareness training  
    - C) VPN usage  
    - D) Data encryption  

    _Answered Correctly: A) Network segmentation_  
    _Explanation:_ Network segmentation divides a network into smaller zones, making it harder for attackers to move laterally within the network.

---

11. **Which of the following encryption methods is best suited for encrypting large volumes of data efficiently?**  
    - A) RSA  
    - B) AES  
    - C) ECC  
    - D) DSA  

    _Your Answer: A) RSA_  
    _Correct Answer: B) AES_  
    _Explanation:_ AES (Advanced Encryption Standard) is a symmetric encryption method that is efficient for encrypting large volumes of data, unlike RSA, which is better for secure key exchange.

---

12. **In a SOC, which role is primarily responsible for analyzing incidents and escalating them if necessary?**  
    - A) Security Analyst  
    - B) Incident Response Lead  
    - C) Network Administrator  
    - D) Security Architect  

    _Your Answer: B) Incident Response Lead_  
    _Correct Answer: A) Security Analyst_  
    _Explanation:_ Security analysts are typically responsible for analyzing incidents and determining if they require escalation.

---

13. **What is the primary goal of a red team during a penetration test?**  
    - A) To deploy security solutions  
    - B) To identify vulnerabilities through automated scanning  
    - C) To simulate real-world attacks and test defenses  
    - D) To develop security policies for the organization  

    _Answered Correctly: C) To simulate real-world attacks and test defenses_  
    _Explanation:_ Red teams emulate adversaries to test the effectiveness of an organization's security measures.

---

14. **Which of the following is a key advantage of role-based access control (RBAC) over discretionary access control (DAC)?**  
    - A) It allows users to control access to their own resources.  
    - B) It is more suitable for smaller organizations.  
    - C) It centralizes access management and reduces human error.  
    - D) It allows more flexibility in access control policies.  

    _Your Answer: D) It allows more flexibility in access control policies._  
    _Correct Answer: C) It centralizes access management and reduces human error._  
    _Explanation:_ RBAC provides a structured and centralized way of managing access rights based on roles, reducing the risk of improper access.

---

15. **What is the primary purpose of using data obfuscation techniques?**  
    - A) To compress data for efficient storage  
    - B) To mask data to protect sensitive information  
    - C) To encrypt data for secure transmission  
    - D) To create backup copies of data  

    _Answered Correctly: B) To mask data to protect sensitive information_  
    _Explanation:_ Data obfuscation makes data unintelligible to unauthorized users, often used to protect data in non-production environments.

---

16. **Which of the following describes a *watering hole* attack?**  
    - A) A targeted attack on a specific individual through phishing  
    - B) A cyberattack that involves poisoning a popular website to target its visitors  
    - C) A form of denial-of-service attack against an organization’s website  
    - D) A technique to flood a network with false data  

    _Answered Correctly: B) A cyberattack that involves poisoning a popular website to target its visitors_  
    _Explanation:_ In a watering hole attack, attackers compromise a website frequently visited by the target group, hoping to infect them.

---

17. **When should an organization conduct a tabletop exercise in incident response?**  
    - A) After an incident occurs  
    - B) During a real-time attack to practice response  
    - C) Periodically as a preparation for potential incidents  
    - D) Only when new vulnerabilities are discovered  

    _Answered Correctly: C) Periodically as a preparation for potential incidents_  
    _Explanation:_ Tabletop exercises help organizations practice their incident response plans in a simulated environment, improving readiness.

---

18. **Which type of malware allows an attacker to control a system remotely without the user’s knowledge?**  
    - A) Rootkit  
    - B) Adware  
    - C) Worm  
    - D) Ransomware  

    _Answered Correctly: A) Rootkit_  
    _Explanation:_ Rootkits are designed to hide their presence on a system and can provide attackers with remote access.

---

19. **Which of the following is an example of a preventive control?**  
    - A) Intrusion Detection System (IDS)  
    - B) Log analysis  
    - C) Security awareness training  
    - D) Data loss prevention (DLP)  

    _Answered Correctly: D) Data loss prevention (DLP)_  
    _Explanation:_ DLP is a preventive control that helps to ensure sensitive information does not leave the organization.

---

20. **Which of the following protocols can be used to establish a secure connection for transferring files over an insecure network?**  
    - A) FTP  
    - B) SFTP  
    - C) Telnet  
    - D) HTTP  

    _Answered Correctly: B) SFTP_  
    _Explanation:_ SFTP uses SSH to provide a secure method of transferring files over an insecure network, unlike plain FTP.

---

21. **What is the main objective of a *gap analysis* in a security audit?**  
    - A) To identify network performance issues  
    - B) To measure compliance with legal requirements  
    - C) To find differences between current and desired security posture  
    - D) To evaluate user satisfaction with security measures  

    _Answered Correctly: C) To find differences between current and desired security posture_  
    _Explanation:_ A gap analysis identifies the gaps between the current security state and the desired state, allowing organizations to plan improvements.

---

22. **Which technique is commonly used to mitigate SQL injection vulnerabilities?**  
    - A) Input validation  
    - B) Enabling HTTP Strict Transport Security (HSTS)  
    - C) Using SSL/TLS  
    - D) Implementing role-based access control  

    _Answered Correctly: A) Input validation_  
    _Explanation:_ Proper input validation prevents attackers from injecting SQL commands into input fields, protecting databases.

---

23. **Which of the following is an example of an insider threat?**  
    - A) A hacker breaking into a company’s network  
    - B) A competitor attempting to steal trade secrets  
    - C) An employee leaking confidential information  
    - D) A ransomware attack from an external source  

    _Answered Correctly: C) An employee leaking confidential information_  
    _Explanation:_ Insider threats involve individuals within the organization who misuse their access to cause harm.

---

24. **In a PKI system, what is the role of a registration authority (RA)?**  
    - A) To sign digital certificates  
    - B) To validate user identities before issuing certificates  
    - C) To store private keys securely  
    - D) To encrypt data using public keys  

    _Answered Correctly: B) To validate user identities before issuing certificates_  
    _Explanation:_ The RA is responsible for verifying the identity of users before the CA issues a certificate to them.

---

25. **Which of the following best describes a *honeypot*?**  
    - A) A decoy system used to attract attackers  
    - B) A system designed to handle large volumes of network traffic  
    - C) A security mechanism that limits user access  
    - D) A software solution for encrypting sensitive data  

    _Answered Correctly: A) A decoy system used to attract attackers_  
    _Explanation:_ Honeypots are decoy systems designed to lure attackers and study their techniques without risk to critical systems.

---

26. **Which hashing algorithm is most vulnerable to collision attacks?**  
    - A) SHA-256  
    - B) SHA-3  
    - C) MD5  
    - D) AES  

    _Answered Correctly: C) MD5_  
    _Explanation:_ MD5 is vulnerable to collision attacks, where two different inputs produce the same hash value.

---

27. **What is the purpose of a *phishing simulation* within an organization?**  
    - A) To improve network performance  
    - B) To test and educate users on recognizing phishing attempts  
    - C) To encrypt email communications  
    - D) To analyze firewall configurations  

    _Answered Correctly: B) To test and educate users on recognizing phishing attempts_  
    _Explanation:_ Phishing simulations are used to improve employees' ability to recognize phishing attacks and avoid falling for them.

---

28. **In the context of incident response, what does the term *containment* refer to?**  
    - A) Identifying the root cause of an attack  
    - B) Isolating affected systems to prevent further spread  
    - C) Restoring systems to a functional state  
    - D) Notifying stakeholders about a breach  

    _Answered Correctly: B) Isolating affected systems to prevent further spread_  
    _Explanation:_ Containment involves isolating compromised systems to stop the spread of an incident while assessing its impact.

---

29. **Which of the following methods can be used to prevent *man-in-the-middle* attacks?**  
    - A) Data obfuscation  
    - B) Using strong passwords  
    - C) Mutual authentication and encryption  
    - D) Disabling unused ports  

    _Answered Correctly: C) Mutual authentication and encryption_  
    _Explanation:_ Mutual authentication ensures both parties verify each other's identities, and encryption protects data from interception.

---

30. **Which of the following scenarios best demonstrates the use of non-repudiation?**  
    - A) Encrypting data with a shared key  
    - B) Implementing a firewall to block unauthorized access  
    - C) Using digital signatures to verify the sender of an email  
    - D) Setting up multifactor authentication for access control  

    _Answered Correctly: C) Using digital signatures to verify the sender of an email_  
    _Explanation:_ Non-repudiation ensures that the sender of a message cannot deny having sent it, achieved through digital signatures.

---

**Score: 27/30**  
**Percentage: 90%**

---
