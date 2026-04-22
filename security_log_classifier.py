def main():

    with open("logins.txt") as f:
        lines = f.readlines()
    # Verifies the number of login records received.
    print(f"Loaded {len(lines)} login records.")

    failed_attempts = {}
    #With Gemini's help, creating a library for the file.

    successful_logins = 0
    failed_logins = 0
    internal_ip = 0
    external_ip = 0


    for line in lines:
        # Got help on this for loop from Gemini when I couldn't find the problem: https://gemini.google.com/app/74a79e4501f23ac4 -- now I feel dumb, because all I had to do was initialize my declared variables outside of the for loop entirely so they wouldn't reset!!
        parts = line.strip().split()
        username = parts[0]
        ip_addr = parts[1]
        status = parts[2]

        # parts = [username, ip, result]
        # print(parts) # used to see inputs to this list variable
    
        if status == "FAILURE":
            key = (username, ip_addr)
            if key in failed_attempts:
                failed_attempts[key] += 1
                failed_logins += 1
            else:
                failed_attempts[key] = 1
                failed_logins = 1
        else:
            successful_logins += 1
        # print(f"Failed logins: {failed_logins}")
        # print(f"Successful logins: {successful_logins}")

        if ip_addr.startswith("192.168.") or ip_addr.startswith("172.16") or ip_addr.startswith("10."):
            internal_ip += 1
        else:
            external_ip += 1

        # print(f"Internal IPs: {internal_ip}")
        # print(f"External IPs: {external_ip}")

    print("-" * 25)
    print("Login Attempts Report")
    print("-" * 25)
    print(f"Total login attempts: {len(lines)}")
    print(f"Successful logins: {successful_logins}")
    print(f"Failed logins: {failed_logins}")
    print(f"Attempts from internal IPs: {internal_ip}")
    print(f"Attempts from external IPs: {external_ip}")

    for (user, ip), count in failed_attempts.items():
        if count >= 3:
            print("+" * 25)
            print(f"Warning: username {user} had {count} failed login attempts from IP address {ip}. Possible brute force attempt.")

    save = input("Do you want to save this information to a file? ")

    if save.lower() == "yes" or "y":
        filename = input("What would you like to name the output file? ")
        output_file = filename + ".txt"
        with open(output_file, "w") as f:
            f.write("-" * 25)
            f.write("\nLogin Attempts Report")
            f.write("\n-" * 25)
            f.write(f"\nTotal login attempts: {len(lines)}")
            f.write(f"\nSuccessful logins: {successful_logins}")
            f.write(f"\nFailed logins: {failed_logins}")
            f.write(f"\nAttempts from internal IPs: {internal_ip}")
            f.write(f"\nAttempts from external IPs: {external_ip}")
            for (user, ip), count in failed_attempts.items():
                if count >= 3:
                    f.write("\n")
                    f.write("+" * 25)
                    f.write(f"\nWarning: username {user} had {count} failed login attempts from IP address {ip}. Possible brute force attempt.")
        print(f"Report saved successfully to {output_file}.")
    else:
        print("Report complete.")
             

if __name__ == '__main__':
    main()